import streamlit as st
from streamlit_chat import message
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Replicate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os
import pandas as pd
from dotenv import load_dotenv
import tempfile


load_dotenv()


def initialize_session_state():
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello! How can I assist you? 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey! 👋"]


def conversation_chat(query, chain, history):
    result = chain({"question": query, "chat_history": history})
    history.append((query, result["answer"]))
    return result["answer"]


def display_chat_history(chain):
    reply_container = st.container()
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Question:", placeholder="Ask about movie booking", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            with st.spinner('Generating response...'):
                output = conversation_chat(user_input, chain, st.session_state['history'])

            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with reply_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="thumbs")
                message(st.session_state["generated"][i], key=str(i), avatar_style="fun-emoji")


def create_conversational_chain(vector_store):
    load_dotenv()
    llm = Replicate(
        streaming=True,
        model="replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781",
        callbacks=[StreamingStdOutCallbackHandler()],
        model_kwargs={"temperature": 0.01, "max_length": 500, "top_p": 1}
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(llm=llm, chain_type='stuff',
                                                 retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
                                                 memory=memory)
    return chain


def main():
    load_dotenv()
    initialize_session_state()
    st.title("Book your favourite shows and events 🎞🎟🎫🎭🎪")

    # Load your local CSV dataset
    csv_path = "concept_description_pairs.csv"  # path/to/your/dataset.csv
    df = pd.read_csv(csv_path)

    # Assuming your CSV has a column named "text" containing the document text
    text_chunks = df["text"].tolist()

    # Ensure text_chunks is a flat list of strings
    text_chunks = [str(chunk) for chunk in text_chunks]

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})

    # Create embeddings for each text chunk
    chunk_embeddings = [embeddings.get_text_embedding(text) for text in text_chunks]

    # Flatten the list of embeddings
    flat_embeddings = [emb for sublist in chunk_embeddings for emb in sublist]

    # Create vector store using the flattened embeddings
    vector_store = FAISS.from_embeddings(flat_embeddings)
    chain = create_conversational_chain(vector_store)

    display_chat_history(chain)



if __name__ == "__main__":
    main()
