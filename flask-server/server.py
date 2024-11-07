from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #Enables CORS for all routes

@app.route('/compoundName', methods=['POST'])
def get_compoundName():
    data = {"message": "Hello from the server!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)