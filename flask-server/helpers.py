from io import open

def match_picto(picto_txt): # Turns explicit to code name

    match (picto_txt):
        case "Explosive":
            return "GHS01"
        case "Flammable":
            return "GHS02"
        case "Oxidizer":
            return "GHS03"
        case "Compressed Gas":
            return "GHS04"
        case "Corrosive":
            return "GHS05"
        case "Acute Toxic":
            return "GHS06"
        case "Irritant":
            return "GHS07"
        case "Health Hazard":
            return "GHS08"
        case "Enviromental Hazard":
            return "GHS09"
        

def reformat(compoundContent):
    """
    Turn JSON response into a more manageable data format.
    
    Compound data is indexed in dictionary touples since data 
    changes depending on the reference source.
    """
    
    compoundData = {}
    compoundData['num'] = compoundContent['Record']['RecordNumber']
    compoundData['name'] = compoundContent['Record']['RecordTitle']
    compoundData['refs'] = [{ref['ReferenceNumber']:ref['SourceName']} for ref in compoundContent['Record']['Reference']]
    
    # Shorten the dict to facilitate address
    shortCmpCont = compoundContent['Record']['Section'][0]['Section'][0]['Section'][0]['Information']
    
    for cont in shortCmpCont:

        # Dict conts indexed with touples since the data is dependent on the reference number
        if cont['Name'] == "Precautionary Statement Codes":
        
            compoundData[('Pcodes',f"{cont['ReferenceNumber']}")] = cont['Value']['StringWithMarkup'][0]['String'].split(", ")
        
        elif cont['Name'] == "Pictogram(s)":

            # Extracts only the name of the pictogram from the list of dicts
            compoundData[('Pictograms',f"{cont['ReferenceNumber']}")] = [match_picto(item['Extra']) for item in cont['Value']['StringWithMarkup'][0]['Markup']]
        
        elif cont['Name'] == "GHS Hazard Statements":

            hazards = cont['Value']['StringWithMarkup']
            compoundData[('Hcodes',f"{cont['ReferenceNumber']}")] = [item['String'].split(":")[0].split(" ")[0] for item in hazards] # Lazy solution

        elif cont['Name'] == "Signal":

            compoundData[('Signal',f"{cont['ReferenceNumber']}")] = cont['Value']['StringWithMarkup'][0]['Markup'][0]["Extra"].strip("GHS")

    return print(compoundData)

# Dictionary class
class CodeDict:
    
    """
    Generates Dictionary object for accesing each code content
    """

    def __init__(self, path="flask-server/resources/dictionary/ghscode_10.txt"):
        
        self.code = [] #GHS Codes (Pcodes, Hcodes)
        self.statement = [] #Hazard Statement
        self.clase = [] #GHS Hazard Class (ie. Explosives, Flammable gases)
        self.category = [] #GHS Hazard Category
        self.div = [] #UN Model Regulations class or Division
        self.pictogram = [] # GHS Pictogram
        self.signal_p = [] # GHS Signal Word

        with open(path, 'r') as fichero:
            for line in fichero:
                if line.strip():
                    parts = line.split("\t")
                    self.code.append(parts[0])
                    self.statement.append(parts[1])
                    self.clase.append(parts[2])
                    self.category.append(parts[3])
                    self.div.append(parts[4])
                    self.pictogram.append(parts[5])
                    self.signal_p.append(parts[6])
