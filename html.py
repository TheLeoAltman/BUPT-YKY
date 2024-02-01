#coding=utf-8
from bs4 import BeautifulSoup
import codecs
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
# 打开HTML文件
class html:
    def __init__(self, path, filename):
        in_path = path + '/' +filename
        length = len(filename)
        for i in range(length - 1, -1, -1):
            if filename[i] == '.':
                break
        out_path = 'trans/'
        for j in range(0, i + 1):
            out_path = out_path + filename[j]
        out_path += 'txt'
        with open(in_path, 'r', encoding='utf-8') as html_file:
            # 读取HTML内容
            html_content = html_file.read()
        # 创建BeautifulSoup对象
        soup = BeautifulSoup(html_content, 'html.parser')

        # 获取文本内容
        html = soup.get_text()
        txt_text = "".join([s for s in html.splitlines(True) if s.strip()])

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(txt_text)
        txt = codecs.open(out_path, 'r', encoding='utf-8')
        data = ''
        for line in txt.readlines():
            line = line.strip()
            data += line + '\n'
        txt.close()
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(data)