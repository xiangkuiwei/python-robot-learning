"""
RNN案例: 基于杰伦歌词来训练模型 用给定的起始词 结合长度 来进行AI歌词生成
实现步骤:
    1.获取数据 进行分词 获取词表
    2.数据预处理 构建数据集
    3.搭建RNN神经网络
    4.训练模型
    5.模型预测
"""

# 导包 
import torch
import jieba
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim
import time

# 1.获取数据 进行分词 获取词表
def bulid_vocab():
    # 1.定义变量 记录去重后所有的词 每行文本分词结果
    unique_words,all_words = [],[]
    # 2.遍历数据集 获取到每行文本
    for line in open('./data/jaychou_lyrics.txt','r',encoding='utf-8'):
        # 2.1获取到每行歌词 进行分词
        words = jieba.lcut(line)
        # 2.2所有分词结果记录到 all_words 中
        all_words.append(words)
        # 2.3遍历分词结果 去重后 添加到unique_words中
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
    # 3.统计语料中去重后词的数量
    word_count = len(unique_words)
    # 4.构建词表 字典形式 key是词 value是词的索引
    word_to_index = {word:i for i,word in enumerate(unique_words)}
    # 5.歌词文本用词表索引表示
    corpus_idx = []
    # 6.遍历每一行的分词结果
    for words in all_words:
        # 6.1定义变量 记录 词索引列表
        tmp = []
        # 6.2获取每一行的词，并获取相应的索引
        for word in words:
            tmp.append(word_to_index[word])
        # 6.3 在每行词之间 添加空格隔开
        tmp.append(word_to_index[' '])
        # 6.4 获取文档中每个词的索引 添加到corpus_idx中
        corpus_idx.extend(tmp)
        # print(f'corpus_idx:{corpus_idx}')
    # 7.返回结果
    return unique_words,word_to_index,word_count,corpus_idx

# 2.数据预处理 构建数据集
# 定义数据集类 继承(torch.utils.data.Dataset)
class LyricsDataset(torch.utils.data.Dataset):
    # 1.初始化词索引 词个数等
    def __init__(self,corpus_idx,num_chars):
        # 1.1文档数据中词的索引
        self.corpus_idx = corpus_idx
        # 1.2每个句子中词的个数
        self.num_chars = num_chars
        # 1.3 文档数据中词的数量 不去重
        self.word_count = len(self.corpus_idx)
        # 1.4句子数量
        self.number = self.word_count //self.num_chars
    # 2.当使用len(obj)时,自动调用此方法.
    def __len__(self):
        # 返回句子数量
        return self.number
        
    # 3.当使用obj[index]时,自动调用此方法
    def __getitem__(self, idx):
        # idx 指的是词的索引 并将其修正索引值 到 文档的范围里
        # 3.1 确保索引start在合法范围内 避免越界 start是当前样本的起始索引
        start = min(max(idx,0),self.word_count-self.num_chars-1)
        # 3.2 计算当前样本的结束索引
        end = start + self.num_chars
        # 3.3 输入值 从文档中取出 start 到 end 的索引的词 作为x
        x = self.corpus_idx[start:end]
        # 3.4 输出值 
        y = self.corpus_idx[start+1:end+1]
        # 返回张量的形式
        return torch.tensor(x),torch.tensor(y)
    
# 3.搭建RNN神经网络
class TextGenerator(nn.Module):
    # 1.初始化方法
    def __init__(self,unique_word_count):
        # 1.1 初始化父类成员
        super().__init__()
        # 1.2 初始化词嵌入层:预料中的词的数量 词向量的维度 
        self.ebd = nn.Embedding(unique_word_count,128)
        # 1.3 循环网络层: 词向量维度 隐藏层维度256 网络层数1
        self.rnn = nn.RNN(128,256,1)
        # 1.4 输出层: 特征向量维度(和隐藏向量维度一样) 词表中词的个数
        self.out = nn.Linear(256,unique_word_count)

    # 2.前向传播方法
    def forward(self,inputs,hidden):
        # 2.1初始化 词嵌入层处理
        # embd格式:(batch句子的数量 句子的长度 词向量的维度)
        embd = self.ebd(inputs)
        # 2.2 rnn处理
        # rnn格式:(句子的长度 batch句子的数量 隐藏层维度)
        output, hidden = self.rnn(embd.transpose(0,1),hidden)
        # 2.3 全连接 输入内容必须是二维数据 即 词的数量*词的维度
        output = self.out(output.reshape(shape=(-1,output.shape[-1])))
        # 2.4 返回结果
        return output,hidden
    
    # 3.隐藏层的初始方法
    def init_hidden(self,bs):     # batch_size
        # 隐藏层初始化:[网络层数 batch 隐藏层向量维度]
        return torch.zeros(1,bs,256)
    
# 4.训练模型
def train():
    # 1.构建词典
    unique_words,word_to_index,unique_word_count,corpus_idx = bulid_vocab()
    # 2.获取数据集
    lyrics = LyricsDataset(corpus_idx,32)
    # 3.初始化神经网络模型
    model = TextGenerator(unique_word_count)
    # 4.创建数据加载器对象
    lyrics_dataloader = DataLoader(lyrics,batch_size=5,shuffle=True)
    # 5.定义损失函数
    criterion = nn.CrossEntropyLoss()
    # 6.定义优化器
    optimizer = torch.optim.Adam(model.parameters(),lr=0.01)
    # 7.模型训练
    # 7.1定义变量 记录训练的轮数
    epochs = 10
    # 7.2 具体的每轮训练动作
    for epoch in range(epochs):
        # 7.3 定义变量记录 本轮开始训练时间 迭代(批次)次数 训练总损失
        start,iter_num,total_loss = time.time(),0,0.0
        # 7.4 具体的 本轮 各批次 训练动作
        # 遍历数据集 后台会调用LyricsDataset#__getitem__()方法, 获取到每个样本的数据和标签
        for x,y in lyrics_dataloader:
            # 7.5 获取隐藏层的初始值
            hidden = model.init_hidden(5)
            # 7.6 模型计算
            output,hidden = model(x,hidden)
            # 7.7 计算损失
            # y的形状:(batch批次数, seq_len句子长度, 词向量维度)->换成一维向量->每个词的下表索引
            # output形状为:(seq_len,batch,词向量维度)
            y = torch.transpose(y,0,1).reshape(shape=(-1, ))
            loss = criterion(output,y)
            # 7.8 梯度清零 + 反向传播 + 更新参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # 7.9 累积损伤 和迭代次数
            total_loss += loss.item()
            iter_num += 1
        # 7.10 走到这里说明本轮训练结束 打印本轮的训练信息
        print(f'epoch:{epoch+1},time:{time.time()-start:.2f}s,loss:{total_loss/iter_num:.4f}')
    # 8.走到这里 说明多轮训练结束(模型训练结束) 保存即可
    torch.save(model.state_dict(),'./model/text_generator.pth')

# 5.模型预测
def evaluate(start_word,sentence_length):
    # 1.构建词典
    unique_words,word_to_index,unique_word_count,corpus_idx = bulid_vocab()
    # 2.获取模型
    model = TextGenerator(unique_word_count)
    # 3.加载模型参数
    model.load_state_dict(torch.load('./model/text_generator.pth'))
    # 4.获取隐藏层初始值
    hidden = model.init_hidden(1)
    # 5.将输入的 开始词 转换成 索引
    word_idx = word_to_index[start_word]
    # 6.定义列表 存放:产生词的索引
    generate_sentence = [word_idx] # 开始词的索引
    # 7. 遍历句子的长度 获取到每一个词
    for i in range(sentence_length):
        # 7.1模型预测
        output,hidden = model(torch.tensor([[word_idx]]),hidden)
        # 7.2获取预测结果
        word_idx = torch.argmax(output)
        # 7.3把预测结果添加到列表中
        generate_sentence.append(word_idx)
    # 8.将索引转换成词 并打印
    for idx in generate_sentence:
        print(unique_words[idx],end='')




# 6.测试
if __name__ == '__main__':
    # 1.获取数据 进行分词 获取词表
    # unique_words,word_to_index,word_count,corpus_idx = bulid_vocab()
    # print(f'词的数量:{word_count}')
    # print(f'去重后的词:{unique_words}')
    # print(f'每个词的索引:{word_to_index}')
    # print(f'文档中每个词对应的索引:{corpus_idx}')

    # 2.构建数据集
    # dataset = LyricsDataset(corpus_idx,5)
    # print(f'句子的数量是:{len(dataset)}')
    # x,y = dataset[1]
    # print(f'输入值:{x}')
    # print(f'输出值:{y}')

    # 3.创建模型对象
    # model = TextGenerator(word_count)
    # 查看参数
    # for name,parameter in model.named_parameters():
    #     print(f'参数名称:{name},参数维度:{parameter.shape}')

    # 4.训练并保存模型
    # train()

    # 5.模型测试
    evaluate('星星',10)