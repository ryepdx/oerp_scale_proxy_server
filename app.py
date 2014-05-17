# Explicit import to enable 'python app.py'
import __init__ 

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
