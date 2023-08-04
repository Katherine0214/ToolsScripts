############################ xls2txt: 将每个注释docstring 分别保存到refs.txt中的每一行中  #######################
import xlrd


xls2txt = open("refs.txt",'w',encoding ='utf-8') #创建写入的文件

file = "code2text_python.xlsx"  #要处理的文件路径
data = xlrd.open_workbook(file) #打开excel表格
table = data.sheets()[0]    #读取第一个sheet
rows = table.nrows  #excel文件的行数
cols = table.ncols  #ecel文件的列数

for rownum in range(1,rows):    #读取行
    for colnum in range(2,cols):    #读取第3列
        celldata = table.cell(rownum,colnum).value  #读取单元格数据，数据格式为float，下面判断将整数数据转化为int
        if type(celldata) == float:
            if int(celldata) == celldata:
                celldata = int(celldata)
        celldata = str(celldata)    #将数据转化为字符串，再对其中的换行符进行处理
        celldata = celldata.replace('\n','')   #使用python中字符串函数替换换行符为空格
        xls2txt.write(celldata) #单行中的数据用tab分隔符分离    xls2txt.write(celldata +'\t')
    xls2txt.write('\n') #每行之间使用换行符
print('清洗完毕')
xls2txt.close() #重要，防止内存溢出