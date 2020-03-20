
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "{'id': 1, 'name': 'zhangsan'}"

@app.route('/aaa')
def aaa():
    return "'aaa'"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5003")
