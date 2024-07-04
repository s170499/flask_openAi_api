from flask import Flask, request, jsonify
from . import create_app, db
from models.models import Question

app = create_app()


@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({"error": "Invalid payload, must contain 'question'"}), 400

        question = data['question']

        answer= {"question": question, "answer": "This is a placeholder answer."}

        # Save the question and answer to the database
        question = Question(question=question, answer=answer)
        db.session.add(question)
        db.session.commit()

        return jsonify({"question": question, "answer": answer}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
 
       

  
    



# cd application
# python app.py
#cmd - curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is food?\"}"
