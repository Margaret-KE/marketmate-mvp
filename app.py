import os
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    # Handle the form submission logic here, e.g., store email in a database
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Get the port from the PORT environment variable, defaulting to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run the app on all available IP addresses and the retrieved port
    app.run(host='0.0.0.0', port=port, debug=True)

