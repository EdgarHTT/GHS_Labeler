#helpers.py

def reformat(compoundContent):
    
    compoundData = {}
    compoundData['num'] = compoundContent['Record']['RecordNumber']
    compoundData['name'] = compoundContent['Record']['RecordTitle']
    
    # Shorten the dict to facilitate address
    shortCmpCont = compoundContent['Record']['Section'][0]['Section'][0]['Section'][0]['Information']
    
    for cont in shortCmpCont:

        # Dict conts indexed with touples since the data is dependent on the reference number
        if cont['Name'] == "Precautionary Statement Codes":
        
            compoundData[('Pcodes',f"{cont['ReferenceNumber']}")] = cont['Value']['StringWithMarkup'][0]['String'].split(", ")
        
        elif cont['Name'] == "Pictogram(s)":

            # Extracts only the name of the pictogram from the list of dicts
            compoundData[('Pictograms',f"{cont['ReferenceNumber']}")] = [item['Extra'] for item in cont['Value']['StringWithMarkup'][0]['Markup']]
        
        elif cont['Name'] == "GHS Hazard Statements":

            hazards = cont['Value']['StringWithMarkup']
            compoundData[('Hstatements',f"{cont['ReferenceNumber']}")] = [item['String'] for item in hazards]

        elif cont['Name'] == "Signal":

            compoundData[('Signal',f"{cont['ReferenceNumber']}")] = cont['Value']['StringWithMarkup'][0]['Markup'][0]["Extra"]

    return print(compoundData)