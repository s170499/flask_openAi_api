FROM python:3.9.16

RUN apt-get update && \
    apt-get install -y postgresql-client-13

WORKDIR /app/application
COPY . /app/application

COPY requirements.txt .
RUN pip install -r requirements.txt


EXPOSE 8000

ENV FLASK_APP=app.py
# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
