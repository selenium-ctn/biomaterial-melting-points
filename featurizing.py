import numpy as np
import deepchem as dc

smi = ["C([C@@H]1[C@H]([C@@H]([C@H]([C@@H](O1)O[C@@H]2[C@H](O[C@H]([C@@H]([C@H]2O)O)O[C@@H]3[C@H](OC([C@@H]([C@H]3O)O)O)CO)CO)O)O)O)O"]

featurizer = dc.feat.ConvMolFeaturizer()
f = featurizer.featurize(smi)
print("yeehaw")
print(dir(f[0]))
print(f[0].atom_features)

chembl_tasks, datasets, transformers = dc.molnet.load_chembl(
    shard_size=2000, featurizer="ECFP", set="5thresh", splitter="random")

print("load success")