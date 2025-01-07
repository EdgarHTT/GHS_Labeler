from flask import Flask, request, render_template, jsonify
from jinja2 import FileSystemLoader
from flask_cors import CORS
from helpers import reformat, tofill, toBoxFormat
import requests

app = Flask(__name__)

# Custom template paths
template_dirs = [
    "templates",
    "templates/labels",
    "templates/pictograms"
]

app.jinja_loader = FileSystemLoader(template_dirs)

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


@app.route('/generate', methods=['POST', 'GET'])
def generateLabel():
    if request.method == 'POST':
        
        data = request.get_json()
        newkeys = ["name", "signal", "h_Stat", "p_Stat", "supp_info", "pictograms"]
        content = {}
        
        for index, oldkey in enumerate(data.keys()):
            content[newkeys[index]] = data[oldkey]

        # Adding suffixes to pictograms names
        content["pictograms"] = [picto.strip() + ".svg" for picto in content["pictograms"]]

        # Label_sizes
        l_size = {"width":664, "height":400}

        #Width and heigh of boxes obtained by multiplying the Label size with a percentage
        
        chem_name = toBoxFormat(l_size["width"]*0.5, l_size["height"]*0.1, content["name"])
        signal = toBoxFormat(l_size["width"]*0.5, l_size["height"]*0.1, content["signal"])
        h_stat = toBoxFormat(l_size["width"]*0.5, l_size["height"]*0.3, content["h_Stat"])
        p_stat = toBoxFormat(l_size["width"]*0.5, l_size["height"]*0.4, content["p_Stat"])
        supp_info = toBoxFormat(l_size["width"]*0.95, l_size["height"]*0.04, content["supp_info"])
        
        print(chem_name)
        print(signal)
        print(h_stat)
        print(p_stat)
        print(content["pictograms"])
        return render_template("display_layout.html", opt=1, label_size = l_size, chem_name=chem_name, signal=signal, h_stat=h_stat, p_stat=p_stat, supp_info=supp_info, pictograms=content["pictograms"])
    
    if request.method == 'GET':

        return render_template("display_layout.html", opt=0)

if __name__ == '__main__':
    app.run(debug=True)