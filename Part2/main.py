import jieba.analyse as analyse
import jieba
import pandas as pd
from gensim import corpora, models, similarities
import gensim
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline


train_data_path = "/home/yang/PycharmProjects/NLP_projects/resources/面试-训练测试集.xlsx"

train_data = pd.read_excel(train_data_path)

title_data = train_data['title']
content_data = train_data['content']


stop_words_path = "/home/yang/PycharmProjects/NLP_projects/resources/stopwords-master/百度停用词表.txt"
stop_words = pd.read_csv(stop_words_path,index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')
stop_words = stop_words['stopword'].values

# print(stop_words)

#开始分词
sentences=[]
for content in content_data:
    # print("-------- 该段内容的关键词为----------")
    # keywords = "  ".join(jieba.analyse.extract_tags(content, topK=20, withWeight=False, allowPOS=()))
    # print(keywords)
    segs = jieba.lcut(content)
    segs = [v for v in segs if not str(v).isdigit()]  # 去数字
    segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
    segs = list(filter(lambda x: x not in stop_words, segs))  # 去掉停用词
    sentences.append(segs)

    print(segs)


# #构建词袋模型
# dictionary = corpora.Dictionary(sentences)
# corpus = [dictionary.doc2bow(sentence) for sentence in sentences]
# #lda模型，num_topics是主题的个数，这里定义了5个
# lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)
# #我们查一下第1号分类，其中最常出现的5个词是：
# # print(lda.print_topic(1, topn=5))
# #我们打印所有5个主题，每个主题显示8个词
# for topic in lda.print_topics(num_topics=10, num_words=8):
#     print(topic[1])


