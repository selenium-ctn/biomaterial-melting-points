import pandas as pd 
import numpy as np

def get_mp_cids():
    df = pd.read_csv(filepath_or_buffer="C://Users//selin//Documents//GitHub//biomaterial-melting-points//data//pubchem_mp.csv")
    cids = df['CID'].tolist()

    cid_list = []
    for id in cids:
        new_cid = id[1:-1] 
        mult_cids = new_cid.split(',')
        for m in mult_cids:
            cid_list.append(int(m))

    cid_set = set(cid_list)
    return cid_set