import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:ido1198LOVE@localhost:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
