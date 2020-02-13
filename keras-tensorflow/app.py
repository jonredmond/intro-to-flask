from flask import Flask, jsonify, request
from classifier import classify

app = Flask(__name__)


@app.route('/classify', methods=['POST'])
def classifyImage():
    classify(request.data)
    return "test"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=False)
