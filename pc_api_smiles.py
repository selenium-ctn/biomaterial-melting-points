import json 
import pandas as pd 
import requests
import numpy as np
import pc_mp_set 

with open("cid_list.txt", "r") as f:
    cid_str = f.read()

cid_list = cid_str.split()

df = pd.read_csv(filepath_or_buffer="C://Users//selin//Documents//GitHub//biomaterial-melting-points//data//pubchem_mp.csv")

smiles_list = []
xlogp_list = []
mp_list = [] 
name_list = []
for mol in cid_list:
    curr_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + mol + "/property/IsomericSMILES/TXT"
    response = requests.get(curr_url)
    smiles_list.append(response.text)
    curr_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + mol + "/property/XlogP/TXT" 
    response = requests.get(curr_url)
    xlogp_list.append(response.text)
    lil_lst = []
    for ind, ci in enumerate(df.loc[:, "CID"]):
        if mol in ci:
            name = df.loc[ind, "Name"]
            lil_lst.append(df.loc[ind, "Melting Point"]) 
    name_list.append(name)
    mp_list.append(lil_lst)

dat = np.stack((name_list, cid_list, smiles_list, xlogp_list, mp_list), axis=1)

df = pd.DataFrame(data=dat, columns=["Name", "CID", "SMILES", "XLogP", "Melting Point"])
df.to_csv(path_or_buf="C://Users//selin//Documents//GitHub//biomaterial-melting-points//data//struct_prop_db.csv")


    