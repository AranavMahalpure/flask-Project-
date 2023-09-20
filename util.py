from flask import Flask
from mybase64 import file_contents
app = Flask(__name__)

@app.route("/")
def classify_image():
    return file_contents
app.run()