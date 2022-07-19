import pandas as pd
import json
from itertools import chain
from collections.abc import MutableMapping
import flatdict



# src_path = 'itemdb_fixed.json'

# with open(src_path, 'r') as f:
#     j: dict = json.loads(f.read())

# for k in j.keys():
#     if k == 'defaultProperty':
#         continue
#     t = type(j[k])
#     is_list = t is list

# print(j)

with open("8.4_itemdb_fixed.json") as jsonFile:
    data: dict = json.load(jsonFile)
    itemData = data["itemList"]["equippable"]

    new_file = pd.json_normalize(itemData)
    new_file.to_csv('TEST_FILE_1.csv')

    
def flatten(d,sep="_"):
    import collections

    obj = collections.OrderedDict()

    def recurse(t,parent_key=""):
        
        if isinstance(t,list):
            for i in range(len(t)):
                recurse(t[i],parent_key + sep + str(i) if parent_key else str(i))
        elif isinstance(t,dict):
            for k,v in t.items():
                recurse(v,parent_key + sep + k if parent_key else k)
        else:
            obj[parent_key] = t

    recurse(d)

    return obj

# stuff = flatten(itemData)
# df = pd.DataFrame(stuff, index=[0])
# df.to_csv('TEST_FILE_2.csv')
print(itemData)