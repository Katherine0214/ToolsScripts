################## 读取原SCV文件内容，并向新SCV文件写入新内容 ####################

from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd



device = "cuda" if torch.cuda.is_available() else "cpu"
torch.cuda.set_device(0)

csv = pd.read_csv('code.csv')
csv_rows = len(csv)   # 读取csv文件行数


tokenizer = AutoTokenizer.from_pretrained("../chatglm/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("../chatglm/chatglm2-6b", trust_remote_code=True).half().to(device)


task = "Please give a short description of all the functions of the following code in no more than 100 words in English: "
response_all = []
for i in range(0, csv_rows):    
    code_query = csv.iloc[i, 1]        # 1代表code在第2列
    query =  task + code_query 
    response, history = model.chat(tokenizer, query, history=[])    
    print(response)
    
    response_all.append(response)

dataframe = pd.DataFrame({'comment':response_all})
#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("add_comment.csv")