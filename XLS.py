################## 读取原XLS文件内容，并向其（原XLS）写入新内容 ####################

from transformers import AutoTokenizer, AutoModel
import torch
import xlrd
from xlutils import copy


device = "cuda" if torch.cuda.is_available() else "cpu"
torch.cuda.set_device(0)

xls = xlrd.open_workbook('query.xls')
sheet = xls.sheet_by_name('Sheet1')
nrows = sheet.nrows

wbook = copy.copy(xls) #复制文件并保留格式
wsheet = wbook.get_sheet(0) #打开表单


tokenizer = AutoTokenizer.from_pretrained("../chatglm/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("../chatglm/chatglm2-6b", trust_remote_code=True).half().to(device)


task = "Please give a short description of all the functions of the following code in no more than 100 words in English: "
for i in range(1, nrows):    
    code_query = sheet.cell_value(i, 1)        # 1代表code在第2列
    query =  task + code_query 
    response, history = model.chat(tokenizer, query, history=[])    
    print(response)
    
    wsheet.write(i,7,response)    # 7代表comment放在第8列
wbook.save('query.xls')    