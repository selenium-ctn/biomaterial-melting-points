import json 
import pandas as pd 
import requests
import numpy as np

mp_list = []
name_list = []
cid_list = []

#1 to 27
for ii in range(1, 2):
    curr_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/annotations/heading/Melting%20Point/JSON?heading_type=Compound&page=" + str(ii)
    response = requests.get(curr_url)
    curr_json = json.loads(response.text)
    for jj in range(0, len(curr_json['Annotations']['Annotation'])):
        mp_list.append(curr_json['Annotations']['Annotation'][jj]["Data"][0]["Value"]["StringWithMarkup"][0]["String"])
        name_list.append(curr_json['Annotations']['Annotation'][jj]["Name"])
        try:
            curr_json['Annotations']['Annotation'][jj]["LinkedRecords"]["CID"]
            cid_list.append(curr_json['Annotations']['Annotation'][jj]["LinkedRecords"]["CID"])
        except:
            cid_list.append(None)

mp_list = np.transpose(mp_list)
name_list = np.transpose(name_list)
cid_list = np.transpose(cid_list)

dat = np.stack((name_list, cid_list, mp_list), axis=1)

df = pd.DataFrame(data=dat, columns=["Name", "CID", "Melting Point"])
df.to_csv(path_or_buf="C://Users//selin//Documents//GitHub//biomaterial-melting-points//data//test.csv")