from transformers import LlamaForCausalLM, LlamaTokenizer, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
import streamlit as st
import huggingface_hub

huggingface_hub.login(token="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")


tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Llama-2-7b")
model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b")


 
def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=128)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

st.title("Movie Booking Chatbot")
user_input = st.text_input("Ask a question about movie bookings:")
if user_input:
    response = generate_response(user_input)
    st.write("Response:", response)

train_dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="bookings.csv",
    block_size=128  # Adjust based on model and hardware
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False  # Set mlm=True for masked language modeling
)

training_args = TrainingArguments(
    output_dir="./output",
    overwrite_output_dir=True,
    num_train_epochs=3,  # Adjust based on dataset size and needs
    per_device_train_batch_size=4,  # Adjust based on available memory
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

trainer.train()

trainer.save_model("./fine-tuned-llama")

