import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
excludes = {"二人","其人","州平","长叹","桃园"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "玄德" or word == "玄德曰":
        rword = "玄德"
    elif word == "云长" or word == "关公":
        rword = "关羽"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1 
  
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count =items[i]
    print("{0:<10}{1:>5}".format(word,count))