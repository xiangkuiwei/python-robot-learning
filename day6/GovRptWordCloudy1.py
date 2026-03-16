import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)    # 使用 jieba精确模式 对文本进行分词，返回词语列表
txt = " ".join(ls)    # 用空格连接所有词语，形成空格分隔的字符串（词云要求的格式）
w = wordcloud.WordCloud(font_path = "/Library/Fonts/Arial Unicode.ttf",\
    width = 1000,height = 700, background_color = "white", max_words = 15)
w.generate(txt)
w.to_file("grwordcloud.png")