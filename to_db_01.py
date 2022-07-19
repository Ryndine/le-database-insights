import json
from numpy.core.records import record
from numpy.lib.arraysetops import isin
import pandas as pd
import sqlite3
import tempfile


src_path = 'itemdb_fixed.json'

with open(src_path, 'r') as f:
    j: dict = json.loads(f.read())
    # k: dict = json.load(f)


def rec_dict(obj, lvl=0):
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, list) or isinstance(i, dict):
                rec_dict(i, lvl)
            else:
                pass
                # print('\t'*lvl, i)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            print('\t'*lvl, k)
            if isinstance(v, list) or isinstance(v, dict):
                # rec_dict(v, lvl+1)
                pass
            else:
                pass
                # print('\t'*(lvl+1), v)
            if k == 'disabledBaseTypesToRoll':
                continue
            df = pd.DataFrame(obj[k])
            df = df.transpose()
            df['subItems'] = df['subItems'].apply(lambda x: [v for v in x.values()])
            df = df.explode('subItems')
            # df = pd.json_normalize(data=df, record_path='subItems', meta=['baseTypeName'])
            print(df)
            
            with open(f'{k}.csv', 'w+') as f:
                df.to_csv(f)
            # input('')
    else:
        pass
    # input('')

# determine handler

for k in j.keys():
    # if k == 'defaultProperty':
    #     continue
    if k != 'itemList':
        continue
    t = type(j[k])
    is_list = isinstance(j[k], list)

    ## remove continue to isolate to just dicts or just lists
    if not is_list: #dicts
    #! these are the ugly ones so far
        # some of these want json_normalize(l), some want j[k], etc etc
        # continue
        print(k)
        rec_dict(j[k])
        # l = [i for i in j[k].values()]
        # print(l)
        # print(pd.json_normalize(l))
    elif is_list:  #lists
    #! these are MOSTLY okay like this. some will need more tlc than others
        # ex: abilityPropertyList needs properties split to columns, at least
        continue
        print(k)
        print(pd.DataFrame(j[k]))
