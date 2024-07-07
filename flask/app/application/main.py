from flask import Blueprint, request, jsonify
from . import db
from models import Q_and_A
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
main = Blueprint('main', __name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

@main.route('/', methods=['GET'])
def check():
    return 'OK', 200


@main.route('/ask', methods=['POST'])
def ask():
    try:
        
        data = request.get_json()
        print('\n\nData\n\n',data,'\n\n')
        newQ_and_A = Q_and_A(
            question = data["question"],
            answer = data["answer"],
            timestamp = datetime.ctime
        )
        db.session.add(newQ_and_A)
        db.session.commit()
        return 'new Q&A added', 200
    except Exception as e:
        db.session.rollback()
        return f'An error occurred: {str(e)}', 500



