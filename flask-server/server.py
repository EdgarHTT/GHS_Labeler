from flask import Flask, jsonify, request # type: ignore
from flask_cors import CORS # type: ignore 

app = Flask(__name__)
CORS(app) #Enables CORS for all routes

@app.route('/compoundName', methods=['GET', 'POST'])
def get_compoundName():
    data = request.get_json() #Retrieves JSON data
    print(data["compoundName"])
    return jsonify({"Response": data["compoundName"]})

if __name__ == '__main__':
    app.run(debug=True)