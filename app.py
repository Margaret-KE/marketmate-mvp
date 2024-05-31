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
    app.run(debug=True)
