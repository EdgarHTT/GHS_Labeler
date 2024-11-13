#helpers.py

def reformat(compoundContent):
    
    print(compoundContent['Record'], "\n")
    print("-"*70)
    print(compoundContent['Record'].keys(), "\n")
    print("-"*70)
    
    # Shorten the dict to facilitate address
    shortCmpCont = compoundContent['Record']['Section'][0]['Section'][0]['Section'][0]['Information']
    
    for cont in shortCmpCont:
        if cont['Name'] == "Precautionary Statement Codes":
            print(cont['ReferenceNumber'], cont['Value']['StringWithMarkup'][0]['String'])
        elif cont['Name'] == "Pictograms(s)":
            print(cont['ReferenceNumber'], cont['Value']['StringWithMarkup'][0]['String'])
        elif cont['Name'] == "GHS Hazard Statements":
            hazards = cont['Value']['StringWithMarkup']
            for hazard in hazards:
                print(cont['ReferenceNumber'], hazard['String'])
        else: print(cont, "\n")

    return print("Done")