from flask import Flask

# Create a new Flask app called 'app'
app = Flask(__name__)

# Create root (starting point route)
@app.route('/')
def hello_world():
    return 'Hello world'