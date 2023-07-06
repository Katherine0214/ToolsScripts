import pandas as pd

data_file = 'train-00000-of-00002-3d7babd70b516246.parquet'
data = pd.read_parquet(data_file)
data.to_csv('code-comment.csv')