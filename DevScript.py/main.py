# Importing the required libraries: transformers for GPT-2, and torch for NLP
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def chatbot_response_logic(user_query):
    # Loading the pre-trained GPT-2 model and adding the tokenizer
    # A tokenizer is an essential NLP feature that breaks up text input from the user into parts, called tokens, so the model can understand
    our_models_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(our_models_name)
    model = GPT2LMHeadModel.from_pretrained(our_models_name)

    # Prepare input text for the chatbot, which will prompt the user to give an input
    models_input_text = user_query

    # Tokenizing the input text (breaking it up into parts)
    # This assigns unique numerical IDs for the model's processing
    # "pt" stands for PyTorch, meaning the output will be returned as a PyTorch tensor
    input_text_IDs = tokenizer.encode(models_input_text, return_tensors="pt")

    # Generating a response
    # Here, the model specifies its output's max_length, num_return_sequences (no. of responses: 1),
    # pad_token_id (allows for padding of the user's input text using a pad_token_id).
    # Padding makes sure that all sequence inputs from the user are of the same length by adding special tokens for short inputs,
    # so the input sequence will always have an equal number of tokens and the model will understand
    models_output = model.generate(input_text_IDs, max_length=100, num_return_sequences=1,
                                   pad_token_id=tokenizer.eos_token_id)

    # Decoding the model's response tokens back to text for the user
    models_response_text = tokenizer.decode(models_output[0], skip_special_tokens=True)

    # Returning the model's response
    return models_response_text


# This function takes a user query (as the user for input) and returns the chatbots response.
user_query = "Hi there! How can I help you?"
chatbot_response = chatbot_response_logic(user_query)
print("Ola: " + chatbot_response)

