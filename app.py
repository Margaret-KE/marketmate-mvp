# app.py

from flask import Flask, jsonify
from config import Config  # Import the Config class from config.py

app = Flask(__name__)

# Use the configuration variables from Config class
app.config.from_object(Config)

# Now you can access the configuration variables using app.config
