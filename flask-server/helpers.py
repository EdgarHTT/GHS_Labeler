from io import open
from math import sqrt, floor
import xml.etree.ElementTree as ET
from PIL import ImageFont

def match_picto(picto_txt): # Turns text name to code name

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
        case "Environmental Hazard":
            return "GHS09"
        case _:
            return picto_txt
        

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
            compoundData[('Pcodes',f"{cont['ReferenceNumber']}")][-1] = compoundData[('Pcodes',f"{cont['ReferenceNumber']}")][-1].strip("and  ")
        
        elif cont['Name'] == "Pictogram(s)":

            # Extracts only the name of the pictogram from the list of dicts
            compoundData[('Pictograms',f"{cont['ReferenceNumber']}")] = [match_picto(item['Extra']) for item in cont['Value']['StringWithMarkup'][0]['Markup']]
        
        elif cont['Name'] == "GHS Hazard Statements":

            hazards = cont['Value']['StringWithMarkup']
            compoundData[('Hcodes',f"{cont['ReferenceNumber']}")] = [item['String'].split(":")[0].split(" ")[0] for item in hazards] # Lazy solution

        elif cont['Name'] == "Signal":

            compoundData[('Signal',f"{cont['ReferenceNumber']}")] = cont['Value']['StringWithMarkup'][0]['Markup'][0]["Extra"].strip("GHS")

    return compoundData

# Dictionary class
class CodeDict:
    
    """
    Generates Dictionary object for accesing each code content
    """

    def __init__(self, path="./resources/dictionary/ghscode_10.txt"):
        
        self.statement = {} #Hazard Statement
        self.clase = {} #GHS Hazard Class (ie. Explosives, Flammable gases)
        self.category = {} #GHS Hazard Category
        self.div = {} #UN Model Regulations class or Division
        self.pictogram = {} # GHS Pictogram
        self.signal_p = {} # GHS Signal Word

        with open(path, 'r') as fichero:
            for line in fichero:
                if line.strip():
                    parts = line.split("\t")
                    # parts[0] is the GHS Code
                    self.statement[parts[0]] = parts[1]
                    self.clase[parts[0]] = parts[2]
                    self.category[parts[0]] = parts[3]
                    self.div[parts[0]] = parts[4]
                    self.pictogram[parts[0]] = parts[5]
                    self.signal_p[parts[0]] = parts[6]

def tofill(compoundData, ref_source = 0, supplier_info = "NaN"):

    dictionary = CodeDict()
    labelContent = {}

    for key in compoundData['refs'][ref_source]: ref = str(key) # declare key name

    # 1.- Product Identifier
    labelContent["name"] = compoundData["name"]
    
    # 2.- Signal Word
    labelContent["signal"] = compoundData['Signal',f'{ref}']
    
    # 3.- Hazard Statement(s)
    hazard_statement = ""
    for index, Hcodes in enumerate(compoundData['Hcodes',f'{ref}']):
        
        hazard_statement += f"{dictionary.statement[f'{Hcodes}']}"
        
        if index != (len(compoundData['Hcodes',f'{ref}']) - 1):
            hazard_statement += "; "
        else:
            hazard_statement += "."
    labelContent["h_Stat"] = hazard_statement

    # 4.- Precautionary Statements
    precautionary_statement = ""
    for index, Pcodes in enumerate(compoundData['Pcodes',f'{ref}']):
        
        precautionary_statement += f" {dictionary.statement[f'{Pcodes}']}"

    labelContent["p_Stat"] = precautionary_statement.strip()

    # 5.- Supplier Information
    labelContent["supp_info"] = supplier_info
    
    # 6.- Pictograms
    labelContent["pictograms"] = compoundData['Pictograms',f'{ref}']

    print(labelContent)

    return labelContent

""" Text Box line wrapper tools"""
# Variables to use

# SVG: width, height

# Wrapping text box: box_width, box_height, font_size, text line list

# Actions to do: separate input text and separate into lines of a 
# maximum number of letters, Calculate font_size by using box_height, box_width
# and number of lines (len(lines))

# Functions: 
# textToLines (str: text, int: box_width, num: char_limit) return (text list)
# toBoxFormat (int: box_width, int: box_height, txtList: textToLines) return (dic: )

def textToLines (box_width: float, text: str, font_size = 8.0) -> list:
    """ Formats text input into a list of lines with a certain char limit"""
    
    # Approximate maximum characters per line
    max_chars = floor((box_width / font_size * 1.83)) # To get an approximate width from font_size
    words = text.split()
    lines, current_line = [], []

    for word in words:
        if sum(len(w) for w in current_line) + len(word) <= max_chars:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line and len(current_line) != 1:
        lines.append(" ".join(current_line))
    else:
        lines = current_line
    
    return lines

def toBoxFormat (box_width: float, box_height: float, text = "NaN") -> dict:
    """ Generates a dict with the data needed to configure the SVG Template 
        Requires: box_width, box_height, and text.
    """
    
    area = box_width * box_height
    font_size = sqrt(area / len(text)) # Assuming each word is a box
    font_size = max(min(font_size, box_height), 8) # Ensure min font size.
    textList = textToLines(box_width, text, font_size)

    formatValues = {}
    formatValues["box_width"] = box_width
    formatValues["box_height"] = box_height
    formatValues["font_size"] = font_size
    formatValues["textList"] = textList
    
    return formatValues


def get_bounding_box(svg_file, l_dims):
    # Font file
    font_file = r'flask-server\resources\fonts\arial.ttf'

    # SVG file parse
    root = ET.fromstring(svg_file)
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    # Text element iteration
    for text_elem in root.findall('.//*[@id="chem_name"]/svg:text', ns):
        text = text_elem.text
        x = (float(text_elem.get('x', '0').strip('%'))/100)*l_dims['width']
        y = (float(text_elem.get('y', '0').strip('%'))/100)*l_dims['height']
        font_size = float(text_elem.get('font-size', '16')) # Default font size

        # Load the font
        font = ImageFont.truetype(font_file, int(font_size))

        # calc txt dims
        bbox = font.getbbox(text)

        # Calculate the bbox
        #bbox = (x, y - text_height, x + text_width, y)
        print(f"Text: {text}, Bounding Box: {bbox}")