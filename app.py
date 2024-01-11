from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the app on localhost (0.0.0.0 means all available network interfaces)
    # and listen on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
