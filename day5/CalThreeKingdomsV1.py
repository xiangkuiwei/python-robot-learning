import jieba
txt = open("threekingdoms.txt","r",encoding = "utf-8").read()
words = jieba.lcut(txt)    # 使用jieba精确模式对文本进行分词，返回列表
counts = {}
for word in words:
    if len(word) == 1:     # 跳过单个字符的词语（如"的"、"了"等无意义词语）
        continue           # 跳过本次循环，不统计单字词  
    else:                  # 统计词频：get(word, 0)获取当前值，不存在则返回0，然后+1
        counts[word] = counts.get(word,0)+1 

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse =True)
for i in range(15):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))