"""
RNN: 循环神经网络 Recurrent neural network 主要处理序列数据
序列数据:后边的数据对前边的数据有依赖
组成: 词嵌入层 循环网络层 输出层
词嵌入层介绍: 把词或者词对应的索引 转换成 词向量
"""

import torch
import jieba # jieba 分词器
import torch.nn as nn

# 定义函数 用于演示 词嵌入层的API 如何把 词 转换为 词向量
def dm01():
    # 1.定义一句话
    text = '北京冬奥的进度条已经过半，不少外国运动员在完成自己的比赛后踏上归途。'
    # 2.使用jieba分词器
    words = jieba.lcut(text)
    print(f'分词结果:{words}')

    # 3.创建词嵌入层
    # 参1:词表大小 参2:词向量的维度
    embed = nn.Embedding(len(words),4)

    # 4.获取每个词对象的下表索引
    # enumerate() 返回列表中 每个值 及其 索引
    for i, word in enumerate(words):
        # 5.要把词索引转换成词向量
        word_vector = embed(torch.tensor(i))
        print(f'词:{word},\t\t 词向量:{word_vector}')

# 2测试
if __name__ == '__main__':
    dm01()