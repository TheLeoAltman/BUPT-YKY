#需要转换的文件放在files中，转换后的txt文件储存在trans中
#coding=utf-8
import os
import utils.doc as doc
import utils.pdf as pdf
import utils.excel as excel
import utils.txt as txt
import utils.html as html
path = 'files'
flist = os.listdir(path)
for li in flist:
    filename = li
    extension = os.path.splitext(filename)[1][1:]
    if extension == 'doc' or extension == 'docx':
        if extension == 'doc':
            os.rename(li, li + 'x')
        a = doc.doc(path, li)
        a = doc.form(path, li)
    elif extension == 'pdf':
        a = pdf.pdf(path, li)
    elif extension == 'xlsx' or extension == 'xls':
        a = excel.excel(path, li)
    elif extension == 'txt':
        a = txt.txt(path, filename)
    elif extension == 'html':
        a = html.html(path, li)
