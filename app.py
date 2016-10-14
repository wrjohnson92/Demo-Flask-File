from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route("/testing")
def testing():
    return "Testing"


@app.route("/thisworks")
def thisworks():
    return "ThisWorks"


if __name__ == '__main__':
	app.run(debug=True)