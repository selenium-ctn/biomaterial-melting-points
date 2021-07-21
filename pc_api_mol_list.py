import json 
import pandas as pd 
import requests
import numpy as np
import pc_mp_set 

mol_list = ["glucose", "arabinose", "xylose", "galactose", "mannose", "fructose", "fucose", "rhamnose", "apiose", \
"galacturonic acid", "mannuronic acid", "guluronic acid", "cellulose", "beta-d-glucan", "xyloglucan", "starch", "amylose", \
"amylopectin", "inulin", "pectin", "agarose", "alginate", "carrageenan", "galactomannan", "glucomannan", \
"mannan", "pectin", "xylan", "dextran", "cellobiose", "callose", "rhamnogalacturonan", "arabinogalactan"]

mp_cid_set = pc_mp_set.get_mp_cids()
carb_cids = [] 
test = []

for ii in mol_list:
    curr_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/" + ii + "/cids/JSON?name_type=word"
    response = requests.get(curr_url)
    curr_json = json.loads(response.text)
    print(ii)
    for jj in range(0, len(curr_json['IdentifierList']['CID'])):
        curr_cid = int(curr_json['IdentifierList']['CID'][jj])
        #print(curr_cid)
        test.append(curr_cid)
        if curr_cid in mp_cid_set:
            if curr_cid not in carb_cids:
                carb_cids.append(curr_cid)

print(carb_cids)
print(len(carb_cids))