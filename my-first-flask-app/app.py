from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/hello', methods=["GET", "POST"])
@app.route('/hello/<name>', methods=["GET", "POST"])
def hello(name=None):
    if name != None:
        return f"Hello {name}"
    elif request.method == "POST":
        return f"Hello {request.json['name']}"


@app.route('/template')
@app.route('/template/<name>')
def hello_template(name=None):
    return render_template("hello_world.html", name=name)


@app.errorhandler(404)
def not_found(err):
    return "You meant to hit /hello-world"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
