<!-- index.html or script.js -->

<script>
    // Function to handle user input and send AJAX request
    function sendMessage() {
        const userQuery = document.getElementById("user-input").value;
        const chatbox = document.getElementById("chat-messages");

        // Append user query to chatbox
        const userMessage = document.createElement("p");
        userMessage.innerHTML = "You: " + userQuery;
        chatbox.appendChild(userMessage);

        // AJAX request to Flask backend
        fetch('/get_response', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 'user_query': userQuery })
        })
        .then(response => response.json())
        .then(data => {
            // Append chatbot response to chatbox
            const chatbotMessage = document.createElement("p");
            chatbotMessage.innerHTML = "Chatbot: " + data['chatbot_response'];
            chatbox.appendChild(chatbotMessage);
        })
        .catch(error => console.error('Error:', error));

        // Clear user input field
        document.getElementById("user-input").value = "";
    }

    // Trigger sendMessage function on user input (e.g., Enter key press)
    document.getElementById("user-input").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
</script>
