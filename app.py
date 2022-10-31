from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, web! :3'

@app.route('/bye')
def bye():
    return 'Bye! ;-;'

app.run(debug=True)