from flask import Flask
import courseTest
from flask import request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['POST'])
def hello():
    return "Hello, World!"

@app.route("/course", methods=['POST'])
def jobSearch():
    insertValues = request.get_json()
    x1=insertValues['keyword']
    print(x1)
    #courseTest.getCourse(x1)
    return courseTest.getCourse(x1)
