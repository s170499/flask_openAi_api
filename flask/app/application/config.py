import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:123@db:5443/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


