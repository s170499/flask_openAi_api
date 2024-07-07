from flask import request, jsonify, Blueprint
from .app import db
from openai import OpenAI
from dotenv import load_dotenv
import os
from models import QandA
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

main_bp = Blueprint('main', __name__)

@main_bp.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        question = data.get("question")

        if not question:
            return jsonify({"error": "Question is required"}), 400

        
        response = client.chat.completions.create(
            model="text-davinci-003",
            prompt=question,
            max_tokens=100
        )

        answer = answer = response['choices'][0]['message']['content']

        new_qa = QandA(
            question=question,
            answer=answer,
            timestamp=datetime
        )

        db.session.add(new_qa)
        db.session.commit()

        return jsonify({"question": question, "answer": answer}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@main_bp.route('/answers', methods=['GET'])
def list_answers():
    try:
        qa_list = db.session.query(QandA).all()
        return jsonify([{"question": qa.question, "answer": qa.answer, "timestamp": qa.timestamp} for qa in qa_list])
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



