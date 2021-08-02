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
flag = False
for mol in cid_list:
    curr_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + mol + "/property/IsomericSMILES/TXT"
    response = requests.get(curr_url)
    smiles_list.append(response.text)
    curr_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + mol + "/property/XlogP/TXT" 
    response = requests.get(curr_url)
    xlogp_list.append(response.text)
    curr_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/" + mol + "/property/Title/TXT" 
    response = requests.get(curr_url)
    name_list.append(response.text)
    lil_lst = []
    for ind, ci in enumerate(df.loc[:, "CID"]):
        cid_str = ci[1:-1]
        cl = cid_str.split(", ")
        ci_set = set(cl)
        if mol in ci_set:
            #name = df.loc[ind, "Name"]
            lil_lst.append(df.loc[ind, "Melting Point"]) 
            #if not flag:
            #    name_list.append(name)
            flag = True
    if not flag:
        print(mol)
    mp_list.append(lil_lst)
    flag = False 

print(len(name_list))
print(len(cid_list))
print(len(smiles_list))
print(len(xlogp_list))
print(len(mp_list))


dat = np.stack((name_list, cid_list, smiles_list, xlogp_list, mp_list), axis=1)

df = pd.DataFrame(data=dat, columns=["Name", "CID", "SMILES", "XLogP", "Melting Point"])
df.to_csv(path_or_buf="C://Users//selin//Documents//GitHub//biomaterial-melting-points//data//struct_prop_db.csv")


    