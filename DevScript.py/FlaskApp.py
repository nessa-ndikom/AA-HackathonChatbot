from flask import Flask, request, jsonify
from main import chatbot_response_logic

app = Flask(__name__)


@app.route('/get_response', methods=['POST'])
def get_chatbot_response():
    user_query = request.json['user_query']
    chatbot_response = chatbot_response_logic(user_query)
    return jsonify({'chatbot_response': chatbot_response})


if __name__ == '__main__':
    app.run()



from flask import Flask, render_template, request, jsonify
from main import chatbot_response_logic

app = Flask(__name__)

# Route to serve the HTML file (e.g., index.html)
@app.route('/')
def serve_html():
    return render_template('index.html')

# Route to handle AJAX requests from the frontend
@app.route('/get_response', methods=['POST'])
def get_chatbot_response():
    user_query = request.json['user_query']
    chatbot_response = chatbot_response_logic(user_query)
    return jsonify({'chatbot_response': chatbot_response})

if __name__ == '__main__':
    app.run()
