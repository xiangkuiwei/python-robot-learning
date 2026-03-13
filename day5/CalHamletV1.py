def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()  # 全部转换为小写
    for ch in '!"#%$&*()*+-./:;?@[]_|{|}':
        txt = txt.replace(ch," ")  # 将文本中的符号用空格代替
    return txt

hamletTxt = getText()
words = hamletTxt.split() # 用空格分割文本，得到单词列表

counts = {}   # 创建空字典，用于存储单词及其出现次数
for word in words:
     # counts.get(word, 0) 获取当前单词的计数值，如果不存在则返回0
     # 然后加1，再存回字典
    counts[word] = counts.get(word,0)+1

items = list(counts.items())    # 将字典转换为列表，每个元素是(单词, 次数)的元组
items.sort(key = lambda x:x[1], reverse=True)  # 按次数降序排序

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
    # {0:<10} 表示第一个参数左对齐，宽度10；  {1:>5} 表示第二个参数右对齐，宽度5