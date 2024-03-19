DATABASE_HOST = 'localhost'
DATABASE_PORT = 3306
DATABASE_USER = 'margaret'
DATABASE_PASSWORD = 'password'
DATABASE_NAME = 'marketmate'

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
