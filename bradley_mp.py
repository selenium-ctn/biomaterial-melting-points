import pandas as pd
import numpy as np

df = pd.read_excel(io="C://Users//selin//Documents//GitHub//biomaterial-melting-points//data//BradleyMeltingPointDataset.xlsx")

mol_list = ["glucose", "arabinose", "xylose", "galactose", "mannose", "fructose", "fucose", "rhamnose", "apiose", \
"galacturonic acid", "mannuronic acid", "guluronic acid", "glucopyran", "glucofuran" "cellulose", "beta-d-glucan", "xyloglucan", "starch", "amylose", \
"amylopectin", "inulin", "pectin", "agarose", "alginate", "carrageenan", "galactomannan", "glucomannan", \
"mannan", "pectin", "dextran", "cellobiose", "callose", "rhamnogalacturonan", "arabinogalactan"] 

name_list = []
csid_list = []
smiles_list = []
mpC_list = []
for ind, ent in enumerate(df.loc[:, "name"]):
    for mol in mol_list:
        if mol in ent:
            if pd.notna(df.loc[ind, "donotuse"]):
                print(df.loc[ind, "donotuse"])
            name_list.append(df.loc[ind, "name"])
            csid_list.append(df.loc[ind, "csid"])
            smiles_list.append(df.loc[ind, "smiles"])
            mpC_list.append(df.loc[ind, "mpC"])

dat = np.stack((name_list, csid_list, smiles_list, mpC_list), axis=1)
df = pd.DataFrame(data=dat, columns=["Name", "CSID", "SMILES", "Melting Point (C)"])
df.to_csv(path_or_buf="C://Users//selin//Documents//GitHub//biomaterial-melting-points//data//bradley_mp.csv")