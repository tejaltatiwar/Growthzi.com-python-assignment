from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Process the data here, for example, save to a database or send an email
    return f"Thank you {name}, we have received your submission."

if __name__ == '__main__':
    app.run(debug=True)
