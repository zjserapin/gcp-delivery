from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'My name is Zach and I like to make AI Apps'


@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/dog')
def dog():
    return 'My dogs name is Nova'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)