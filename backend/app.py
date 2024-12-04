from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for communication with the React frontend

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Example response (replace with actual Gemini model logic)
    response = {"reply": f"Echo: {user_input}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
