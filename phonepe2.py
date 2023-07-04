import os
import requests
import subprocess

# Clone the Github repository
os.system("git clone https://github.com/PhonePe/pulse.git")

import json
import pandas as pd

# root_dir for AGGREGATED TRANSACTION
root_dir = r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\aggregated\transaction\country\india\state')):
    state_path = os.path.join(root_dir, r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\aggregated\transaction\country\india\state', state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data 
                            for transaction_data in data['data']['transactionData']:
                                row_dict = {
                                    'State': state_dir,
                                    'Year': year_dir,
                                    'Quarter': int(json_file.split('.')[0]),
                                    'Transaction_type': transaction_data['name'],
                                    'Transaction_count': transaction_data['paymentInstruments'][0]['count'],
                                    'Transaction_amount': transaction_data['paymentInstruments'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df1 = pd.DataFrame(data_list)
df1

# root_dir for AGGREGATED USER
root_dir = r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\aggregated\user\country\india\state'
df2_list = []

for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):
        for json_file in os.listdir(state_path):
            if json_file.endswith('.json'):
                with open(os.path.join(state_path, json_file), 'r') as f:
                    json_data = json.load(f)
                    if isinstance(json_data, list):
                        df2_list += json_data
                    else:
                        df2_list.append(json_data)
        if df2_list:
            df2 = pd.json_normalize(df2_list)
            df2['subfolder'] = state_dir
            df2['subsubfolder'] = 'state'
df2 = pd.DataFrame(data_list)

df2
# root_dir for MAP TANSACTION
root_dir = r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data'
# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\map\transaction\hover\country\india\state')):
    state_path = os.path.join(root_dir, r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\map\transaction\hover\country\india\state', state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data
                            for hoverDataList in data['data']['hoverDataList']:
                                row_dict = {
                                    'State': state_dir,
                                    'Year': year_dir,
                                    'Quarter': int(json_file.split('.')[0]),
                                    'District': hoverDataList['name'],
                                    'Transaction_type': hoverDataList['metric'][0]['type'],
                                    'Transaction_count': hoverDataList['metric'][0]['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df3 = pd.DataFrame(data_list)

df3
#root_dir for MAP USER
root_dir = r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\map\user\hover\country\india\state'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data 
                            for district, values in data['data']['hoverData'].items():
                                row_dict = {
                                    'State': state_dir,
                                    'Year': year_dir,
                                    'Quarter': int(json_file.split('.')[0]),
                                    'District': district,
                                    'Registered_users': values['registeredUsers'],
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df4 = pd.DataFrame(data_list)

df4
#root_dir for TOP TRANSACTION
root_dir = r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(os.path.join(root_dir, r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\top\transaction\country\india\state')):
    state_path = os.path.join(root_dir, r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\top\transaction\country\india\state', state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files (one for each quarter)
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data 
                            for districts in data['data']['districts']:
                                row_dict = {
                                    'State': state_dir,
                                    'Year': year_dir,
                                    'Quarter': int(json_file.split('.')[0]),
                                    'District': districts['entityName'],
                                    'Transaction_type': districts['metric']['type'],
                                    'Transaction_count': districts['metric']['count'],
                                    'Transaction_amount': districts['metric']['amount']
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df5 = pd.DataFrame(data_list)

df5
# root_dir for TOP USER
root_dir = r'C:\Users\Vijay Anand\OneDrive\Desktop\pulse-master\pulse-master\data\top\user\country\india\state'

# Initialize empty list to hold dictionaries of data for each JSON file
data_list = []

# Loop over all the state folders
for state_dir in os.listdir(root_dir):
    state_path = os.path.join(root_dir, state_dir)
    if os.path.isdir(state_path):

        # Loop over all the year folders
        for year_dir in os.listdir(state_path):
            year_path = os.path.join(state_path, year_dir)
            if os.path.isdir(year_path):

                # Loop over all the JSON files
                for json_file in os.listdir(year_path):
                    if json_file.endswith('.json'):
                        with open(os.path.join(year_path, json_file)) as f:
                            data = json.load(f)

                            # Extract the data 
                            for district in data['data']['districts']:
                                row_dict = {
                                    'State': state_dir,
                                    'Transaction_Year': year_dir,
                                    'Quarter': int(json_file.split('.')[0]),
                                    'District': district['name'] if 'name' in district else district['pincode'],
                                    'RegisteredUsers': district['registeredUsers'],
                                }
                                data_list.append(row_dict)

# Convert list of dictionaries to dataframe
df6 = pd.DataFrame(data_list)
df6

# Data transformation on file1
# Drop any duplicates
d1 = df1.drop_duplicates()
d2 = df2.drop_duplicates()
d3 = df3.drop_duplicates()
d4 = df4.drop_duplicates()
d5 = df5.drop_duplicates()
d6 = df6.drop_duplicates()

# checking Null values
null_counts = d1.isnull().sum()
print(null_counts)

null_counts = d2.isnull().sum()
print(null_counts)

null_counts = d3.isnull().sum()
print(null_counts)

null_counts = d4.isnull().sum()
print(null_counts)

null_counts = d5.isnull().sum()
print(null_counts)

null_counts = d6.isnull().sum()
print(null_counts)

# converting all dataframes in to csv
d1.to_csv('agg_trans.csv', index=False)
d2.to_csv('agg_user.csv', index=False)
d3.to_csv('map_tran.csv', index=False)
d4.to_csv('map_user.csv', index=False)
d5.to_csv('top_tran.csv', index=False)
d6.to_csv('top_user.csv', index=False)
