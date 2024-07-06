from flask import Blueprint, request, jsonify
import openai
from .models import QuestionAnswer
from . import db
import os

main = Blueprint('main', __name__)

@main.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    # Call OpenAI API
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=50
    )
    answer = response.choices[0].text.strip()

    # Save to database
    qa = QuestionAnswer(question=question, answer=answer)
    db.session.add(qa)
    db.session.commit()

    return jsonify({'question': question, 'answer': answer})



 
       

  
    



# cd application
# python app.py
#cmd - curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is food?\"}"
