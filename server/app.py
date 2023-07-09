from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/create-website", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.get_json())
        return "This is a POST request"


if __name__ == "__main__":
    app.run(port=8080, debug=True)
