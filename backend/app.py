from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Example response (replace with actual Gemini model logic)
    response = {"reply": f"Echo: {model.generate_content(user_input).text}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
