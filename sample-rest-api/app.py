from uuid import uuid4
from flask import Flask, request, jsonify
app = Flask(__name__)

todos = []


@app.route('/todos', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        new_todo = request.json
        new_todo["_id"] = str(uuid4())
        todos.append(new_todo)
        return new_todo
    else:
        return jsonify(todos)


@app.route('/todos/<id>', methods=["GET"])
def get_todo_by_id(id=""):
    return next(todo for todo in todos if todo['_id'] == id)


@app.errorhandler(404)
def not_found(err):
    return "You meant to hit /hello-world"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
