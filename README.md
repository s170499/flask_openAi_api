# flask openAI Q&A back-end server

This project is a simple Flask server that exposes an endpoint to ask a question. The server sends the question to an OpenAI API, receives the answer, and saves both the question and the answer in a PostgreSQL database(I am using an official PostgreSQL-16 image).
The server and the database are dockerized and run with Docker Compose.
Furthermore i used SQLAlchemy for ORM and Alembic for database migrations, and the tests are using pytest.


## Prerequisites
- You will need to have Docker and Docker Compose installed. 
Go to [Docker's website](https://docs.docker.com/get-docker/) and install a version of Docker for your operating system of choice.
- You wiil also need a openAI API key. 
To create a new API key click [here](https://beta.openai.com/account/api-keys).


## Install
1. Clone the repository:
```
git clone https://github.com/s170499/flask_openAi_api.git
```

2. Set up your OpenAI API credentials, there are several options for this:     
**Option 1**: Create a .env file in the root directory of the project with your API key:
```
OPENAI_API_KEY=your_api_key_here
```
**Option 2**:
Set your ‘OPENAI_API_KEY’ Environment Variable on your operating system,       
on command prompt(cmd) or terminal:

```
setx OPENAI_API_KEY “<your-key>”
```

## Usage
To start the project:
```
docker compose up --build
```
To disable application:
```
docker compose down
```
## Run migrations:
```
docker-compose exec web alembic upgrade head
```

## Testing flask
- **Option 1**:You can and should replece the question to test the endpoint.

In Command Prompt run:
```
curl -X POST http://127.0.0.1:8000/ask \ -H "Content-Type: application/json" -d \ '{"content": "How does AI work? Explain it in simple terms."}' \
```
 In PowerShell run:
```
curl -X POST http://127.0.0.1:8000/ask -H "Content-Type:application/json" -d '{\"question\":\"What is the capital of France?\"}'
```

- **Option 2**: Using pytest
```
docker-compose up --build
pytest test.py
```





