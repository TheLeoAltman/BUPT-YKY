import pandas
import os

# 格式转换
class excel :
    def __init__(self, path, filename):
        def Excel_to_Txt(input_path, output_path):
            df = pandas.read_excel(input_path, header=None)
            df.to_csv(output_path, header=None, sep=',', index=False)  # sep指定分隔符，分隔单元格

        # 创建同路径同名TXT文件
        def creat_txt(input_path):
            length = len(input_path)
            output_path = 'trans/'
            for i in range(length - 1, -1, -1):
                if input_path[i] == '.':
                    break
            for j in range(0, i + 1):
                output_path = output_path + input_path[j]
            output_path = output_path + 'txt'
            # file = open(output_path,)
            return output_path

        input_path = path + '/' + filename
        output_path = creat_txt(filename)
        Excel_to_Txt(input_path, output_path)