from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

from openai import OpenAI

import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB Setup
mongodb_uri = "mongodb+srv://tako1201:q4ZSsjP7A8j5gWNk@subsidencedata.a9e17.mongodb.net/?retryWrites=true&w=majority&appName=subsidenceData"
client = MongoClient(mongodb_uri)
db = client["dcard"]
daily_collection = db["from0813"]

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Here you should add your authentication logic
    if username == 'test' and password == 'test':  # Example validation
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Home Route
@app.route('/home', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Home Page!"}), 200

# Daily Route - Fetch data from MongoDB
@app.route('/daily', methods=['GET'])
def daily():
    try:
        daily_data = list(daily_collection.find({}, {"_id": 0}))  # Fetch all documents, excluding `_id`
        return jsonify(daily_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/check-connection', methods=['GET'])
def check_connection():
    try:
        # Try to list databases to verify the connection
        client.admin.command('ping')
        return jsonify({"message": "Connection successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/todo', methods=['GET'])
def todo():
    try:
        daily_data = []
        explanations=[]
        for document in daily_collection.find({}, {"_id": 0}):  # Fetch all documents, excluding `_id`
            aiClient = OpenAI(api_key=OPENAI_API_KEY)
            response = aiClient.chat.completions.create(
                model='ft:gpt-4o-2024-08-06:personal::AFkm0nkT',
                messages=[
                    {'role': 'user', 'content': document["content"] + '\r\n這篇文章是否在討論地層下陷議題，請先回答是或否，接著再解釋為什麼'}
                ],
                max_tokens=1500
            )
            response_content = response.choices[0].message.content
            first_two_characters = response_content[:2]
            #print(response_content[:10])
            if "是" in first_two_characters:
                daily_data.append(document)
                explanations.append(response_content)
                #print(f"Relevant document: {document["title"]}")
        return jsonify({"explain": explanations, "data": daily_data}), 200
    except Exception as e:
        #print("An error occurred:", e)
        return jsonify({"message": str(e)}), 500


# @app.route('/test')
# def perform_comment_crawling():
#     for document in daily_collection.find():
#         aiClient = OpenAI(api_key=OPENAI_API_KEY)
#         response = aiClient.chat.completions.create(
#             model='ft:gpt-4o-2024-08-06:personal::AFkm0nkT',
#             messages=[
#                 {'role': 'user', 'content': document["content"] + '\r\n這篇文章是否在討論地層下陷議題，請先回答是或否，接著再解釋為什麼'}
#             ],
#             max_tokens=1500
#         )
#         response_content = response.choices[0].message.content
#         first_two_characters = response_content[:2]
#         print(response_content[:20])
#         if "是" in first_two_characters:
#             print(f"Relevant document: {document["title"]}")
#     return "complete"


if __name__ == '__main__':
    app.run(debug=True)
