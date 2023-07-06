import pandas as pd
 
# json2xlsx
data = pd.read_json('OTA.json')
data.to_excel('OTA.xlsx', index=False)


