# import csv

# with open('equippable.csv') as input, open('equippable-fixed.csv', 'w', newline='') as output:
#      writer = csv.writer(output)
#      for row in csv.reader(input):
#          if any(field.strip() for field in row):
#              writer.writerow(row)

import pandas as pd

# df = pd.read_csv('equippable.csv')
# df.to_csv('equippable_output.csv', index=True)
# df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

# # df.reset_index(drop=True, inplace=False)

# df = df.drop(columns=['size', 'cannotDrop', 'implicits'], axis=1)

# df.to_csv('hateshudmeyer.csv', index=False)

# print(len(df.columns))

df = pd.read_csv('hateshudmeyer.csv')



blessings_df = df[df.baseTypeName == 'Blessing']
# blessings_df.to_csv('blessings_database.csv', index=False)

idol_values = ['Small Idol', 'Small Lagonian Idol', 'Humble Idol','Stout Idol', 'Grand Idol', 'Large Idol', 'Ornate Idol', 'Huge Idol', 'Adorned Idol']
idol_df = df[df.baseTypeName.isin(idol_values) == True]
# idol_df.to_csv('idol_database.csv', index=False)

# non_item_values = ['Blessing', 'Small Idol', 'Small Lagonian Idol', 'Humble Idol','Stout Idol', 'Grand Idol', 'Large Idol', 'Ornate Idol', 'Huge Idol', 'Adorned Idol']
# item_database = df[df.baseTypeName.isin(non_item_values) == False]
# item_database.to_csv('item_database.csv', index=False)

# df.append([df[df['IsHoliday'] == True]] * 5, ignore_index=True)

item_database = pd.read_csv('item_database.csv')
unique_database = pd.read_csv('unique_database.csv')
# unique_database = df[df['uniques.1.displayName'].notnull()]
# unique_database = unique_database.drop(columns=['displayName'])
# unique_database = unique_database.rename(columns={'uniques.1.displayName' : 'displayName'})
# unique_database.to_csv('unique_database.csv', index=False)

# print(unique_database)

# df_merged = pd.merge(item_database, unique_database, on=['Base Type', 'subTypeId'], how='left')
# df_joined = item_database.join(unique_database, on='Base Type ID', how='outer')
df_concat = pd.concat([item_database, unique_database], ignore_index=True)
# df_merged.to_csv('df_merged.csv', index=False)
# df_joined.to_csv('df_joined.csv', index=False)
df_concat.to_csv('df_concat.csv', index=False)

print(unique_database.dtypes)
