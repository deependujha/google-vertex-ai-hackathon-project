from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/create-website", methods=["POST"])
def home():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        file_path = './myZip.zip'
    
        # Send the file to the frontend
        return send_file(file_path, as_attachment=True)
        # return "This is a POST request"


if __name__ == "__main__":
    app.run(port=8080, debug=True)
