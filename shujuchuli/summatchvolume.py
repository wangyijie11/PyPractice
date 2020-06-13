import pandas as pd
import numpy as np
import os


# 获取指定目录下的文件ming
def getfilenames(filepath):
    result = []
    file_path = filepath
    file_list = os.listdir(filepath)
    for file in file_list:
        abspath = os.path.join(file_path, file)
        if os.path.isfile(abspath):
            result.append(abspath)
    return result


# 读取文件内容，读取时进行更多的处理，可以减少后续清理操作
def readfile(file):
    data = pd.read_csv(file)
    print(data.head())
    return data


def groupby(file):
    data = pd.read_csv(file)
    data_trade = data[data['function_code'] == '0']
    print(data_trade)
    result = data_trade.groupby('symbol')['volume'].apply(lambda x: x.sum())
    print(data_trade.groupby('symbol').tail(1))
    return result

if __name__ == "__main__":
    filenames = getfilenames("../shujuyangben")
    print(filenames)
    for name in filenames:
        result = groupby(name)
        print(result)