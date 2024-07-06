from flask import Flask, request, jsonify
import openai
from openai import OpenAI
from app.flask.app.application.models import Question
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
db = SQLAlchemy()

@app.route('/ask', methods=['POST'])
def ask():
    
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({"error": "Invalid payload, must contain 'question'"}), 400

        question = data['question']
        completion = client.chat.completions.create(
             model="gpt-3.5-turbo", messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say this is a test"}
        ,],)

        # Extract the answer from the API response
        answer = completion.choices[0].message.content

        return jsonify({"question": question, "answer": answer}), 200

    except Exception as e:
        # Save the question and answer to the database
        question = Question(question=question, answer="I am a greeedy little cunt")
        db.session.add(question)
        db.session.commit()
        return jsonify({"question": question, "answer": "I am a greeedy little cunt"}), 200
        # return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)

