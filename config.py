from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DATABASE_HOST = ('LOCALHOST')
DATABASE_PORT = (3306)

class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key_here'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'username'
    MYSQL_PASSWORD = 'password'
    MYSQL_DB = 'database_name'
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
