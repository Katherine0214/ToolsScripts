############################ txt2csv: 将txt每行放入csv指定列中  #######################
import pandas as pd
import linecache


filename = 'CN_comment.txt'
file = open(filename,'r',encoding ='utf-8') 
countline_comment = len(file.readlines())

CN_comment_all = []
for i in range(1, countline_comment):    
    CN_comment = linecache.getline(filename, i)
    CN_comment_all.append(CN_comment)
    
dataframe = pd.DataFrame({'CN_comment':CN_comment_all})
#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("CN_comment.csv", encoding='utf-8', index=True)   