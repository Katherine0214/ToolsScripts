################## 读取原TXT文件内容，并向新TXT文件写入新内容 ####################

from transformers import AutoTokenizer, AutoModel
import torch
import linecache
import pandas as pd


device = "cuda" if torch.cuda.is_available() else "cpu"
torch.cuda.set_device(1)


filename = 'query.txt'
file = open(filename,'r',encoding ='utf-8') 
countline_query = len(file.readlines())

pred = open("pred.txt",'a',encoding ='utf-8') #创建写入的文件

tokenizer = AutoTokenizer.from_pretrained("../chatglm/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("../chatglm/chatglm-6b", trust_remote_code=True).half().to(device)


task = "Please give a short description of all the functions of the following code in no more than 100 words in English: "
for i in range(1, 89):    # 90
    code_query = linecache.getline(filename, i)
    query =  task + code_query 
    response, history = model.chat(tokenizer, query, history=[])    
    print(response)
    
    pred.write(response + '\n')  # + '\n'
pred.close()    