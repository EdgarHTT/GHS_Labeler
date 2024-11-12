
def reformat(compound):
    compoundDict = {}
    
    # Record number
    compoundDict['RecNumber'] = compound['Record']['RecordNumber']
    # Compound name
    compoundDict['name'] = compound['Record']['RecordTitle']