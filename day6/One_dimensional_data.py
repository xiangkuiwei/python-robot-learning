# 采用空格分隔的方式将数据写入文件
ls = ['中国','美国','日本']
fname = []
f = open(fname, 'w')
f.write(''.join(ls))
f.close

# 采用特殊分隔方式将数据写入文件
ls = ['中国','美国','日本']
fname = []
f = open(fname, 'w')
f.write('$'.join(ls))
f.close

# 从CSV格式的文件中读入数据
fo = open(fname)
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
fo.close

# 将数据写入CSV格式
ls = [[],[],[]]
f = open(fname,'w')
for item in ls:
    f.write(','.join(item)+'\n')
f.close()

# 采用二层循环遍历二维数据的每个元素
ls = [[1,2],[3,4],[5,6]]
for row in ls:
    for column in row:
        print(column)