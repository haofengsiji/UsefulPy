#CalStatistics_Data.py
import jieba
import pandas as pd
import os
# read all files in the folder
entries = os.listdir('data/')
# calculate word frequency by loops
counts = {}
# pre_data.txt contains masked words
pre_data = open("pre_data.txt",encoding="utf-8").read()
excludes = jieba.lcut(pre_data) # the masked words
for file in entries:
    # read the data in file
    data = open(os.path.join('data',file),"r",encoding="utf-8").read()
    # replace 012345678 as empty space
    for ch in '0123456789':
        data = data.replace(ch," ")
    # use jieba cut text
    words = jieba.lcut(data) # words requiring statistics
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1
    for i in excludes:
        if i in counts:
            del counts[i]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse = True)
df1 = pd.DataFrame(items,
                columns=['Word', 'Num.'])
df1.to_excel("output.xlsx",index=False)
