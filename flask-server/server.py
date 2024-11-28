from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from helpers import reformat, tofill
import requests

app = Flask(__name__)
CORS(app) #Enables CORS for all routes

@app.route('/fetchCompound', methods=['POST'])
def generationRequest():

    # We get the json data from client query
    data = request.get_json()
    print(data)

    # Create apropiate url format for API target
    api_url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{data}/cids/JSON'
    
    # Make request
    response = requests.get(api_url)

    # Handle response
    if response.status_code == 200:
        
        #Extracting CID
        cid = response.json()
        # Turn to string
        cid = cid['IdentifierList']['CID'][0]
        # Debug log
        app.logger.debug('Compound CID: ', cid)

    else:
        print("Compound not found or an error occurred.", response.status_code)
        return response.status_code
    
    # Create appropiate REST api request for GHS Classification
    api_url_GHS = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON/?response_type=display&heading=GHS%20Classification'

    # Make request
    response_GHS = requests.get(api_url_GHS)

    # Handle non successful response
    if response_GHS.status_code != 200:
        
        print("Compound not found or an error occurred.", response_GHS.status_code)
        return response_GHS.status_code
    
    #app.logger.debug(response_GHS.json())

    # We need to remove all the unneccesary JSON and reorder to a useful format
    compoundData = reformat(response_GHS.json())

    # data to dict for filling the label format
    labelContent = tofill(compoundData, 1)


    return jsonify(labelContent)


@app.route('/generate', methods=['POST'])
def generateLabel():
    
    data = request.get_json()
    newkeys = ["name", "signal", "h_Stat", "p_Stat", "supp_info", "pictograms"]
    content = {}
    for index, oldkey in enumerate(data.keys()):
        content[newkeys[index]] = data[oldkey]
    print(content)
    return request.get_json()

@app.route('/display', methods=['GET'])
def displayRequest():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(debug=True)