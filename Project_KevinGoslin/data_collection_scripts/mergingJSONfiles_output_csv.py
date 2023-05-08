# use to merge json files as array of objects from smart Dublin API calls in to one json file.

import pandas as pd
import glob, os, json


json_dir = '' # directory containing all the json files to be merged

json_pattern = os.path.join(json_dir, '*.json')
file_list = glob.glob(json_pattern)

dfs = []
for file in file_list:
    with open(file) as f:
        json_data = pd.json_normalize(json.loads(f.read()))
    dfs.append(json_data)
df = pd.concat(dfs)

# write the merged data to a csv file
df.to_csv('myfileMerged.csv', sep='\t')
