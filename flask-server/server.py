from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) #Enables CORS for all routes

@app.route('/compoundName', methods=['POST'])
def generationRequest():

    # We get the json data from generateCompound
    data = request.get_json()
    print(data)

    # Create apropiate url format for API target
    api_url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{data['compoundName']}/cids/JSON'
    
    # Make request
    response = requests.get(api_url)

    # Handle response
    if response.status_code == 200:
        
        #Extracting CID
        cid = response.json()
        cid = cid['IdentifierList']['CID']

    else:
        print("Compound not found or an error occurred.", response.status_code)
        return response.status_code

if __name__ == '__main__':
    app.run(debug=True)