from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Worlddddddddddddd -- I am JACK!'

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
