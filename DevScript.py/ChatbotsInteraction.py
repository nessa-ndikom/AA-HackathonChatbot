from main import chatbot_response_logic


# Function to get user input
def get_user_input():
    return input("You: ")


# Main loop to interact with the chatbot
def chatbot_interaction():
    print("Ola: Hi there! How can I help you?")
    while True:
        user_query = get_user_input()
        if user_query.lower() in ['exit', 'quit']:
            print("Ola: Goodbye!")
            break

        chatbot_response = chatbot_response_logic(user_query)
        print("Ola:", chatbot_response)


if __name__ == "__main__":
    chatbot_interaction()
