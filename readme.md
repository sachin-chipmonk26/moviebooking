# install all the dependencies

```pip install -r requirements.txt```

# fine tuning llama 2

```pip install autotrain-advanced```
```pip install huggingface_hub```


# Update .env file with your own api token which can be fetched from the link https://replicate.com/account/api-tokens. You need to sign in with your github account

REPLICATE_API_TOKEN = "Your replicate api token"

# Create a hugging face account and fetch a new User Access Token from the link below 

https://huggingface.co/settings/tokens

# type the command below to login to huggingface using cli
huggingface-cli login
# after typing the above command enter your hugging face token

# To run the application 
```streamlit run app.py```
 
# video references to build this project

## Build a chatbot that accepts multiple docs as datasets with llama2 70b model

https://www.youtube.com/watch?v=vhghB81vViM

## How to Create Custom Datasets To Train Llama-2

https://www.youtube.com/watch?v=z2QE12p3kMM

## The EASIEST way to finetune LLAMA-v2 on local machine!
https://www.youtube.com/watch?v=3fsn19OI_C8
