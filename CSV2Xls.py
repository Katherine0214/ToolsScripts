import xlwt


def csv_xls(filename, xlsname):
    f = open(filename, 'r', encoding='utf-8')
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
    x = 0
    for line in f:

        for i in range(len(line.split(','))):
            print(i)
            item = line.split(',')[i]
            sheet.write(x, i, item)
        x += 1
    f.close()
    xls.save(xlsname)


if __name__ == "__main__":
    filename = "code-comment.csv"
    xlsname ="code-comment.xls"
    csv_xls(filename,xlsname)
