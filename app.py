import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/lib/python2.7/site-packages")

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
