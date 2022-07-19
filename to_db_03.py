import json
from numpy.core.records import record
from numpy.lib.arraysetops import isin
import pandas as pd
import numpy as np
import sqlite3
import tempfile


src_path = '8.4_itemdb_fixed.json'

with open(src_path, 'r') as f:
    j: dict = json.loads(f.read())
    # k: dict = json.load(f)

def horizontal_unnesting(df, explode, axis):
    if axis==1:
        df1 = pd.concat([df[x].explode() for x in explode], axis=1)
        return df1.join(df.drop(explode, 1), how='left')
    else :
        df1 = pd.concat([
        pd.DataFrame(df[x].tolist(), index=df.index).add_prefix(x) for x in explode], axis=1)
        return df1.join(df.drop(explode, 1), how='left')

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
            # print('\t'*lvl, k)
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
            df = df.explode('subItems').reset_index(drop=True, inplace=False)
            normalized = pd.json_normalize(df['subItems'])
            df = df.drop(['displayName'], axis=1).join(normalized).drop(columns=['subItems'])
            df.reset_index(drop=True, inplace=False)
            # df['subItems'] = df['subItems'].fillna({'None':0})

            # pd.DataFrame(np.column_stack((a, vals.ravel())), columns=df.columns)

            # df.set_index(['displayName']).apply(pd.Series.explode).reset_index()

            # df = horizontal_unnesting(df, ['subItems'], axis=0)

            # df1 = df['subitems1']
            # df1 = df.explode('subItems1')
            # df = horizontal_unnesting(df, ['subItems'], axis=0)
            # print(type(df))
            # df.to_dict()
            print(df)
            # for i, r in df.iteritems():
            #     print(r["subItems"])
            # print(df)
            
            with open(f'{k}.csv', 'w+', index=False) as f:
                df.to_csv(f)
                normalized.to_csv('normalized.csv')
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
        # print(k)
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
