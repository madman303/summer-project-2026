import jieba
from collections import Counter

#读取评论
with open("comments.txt","r",encoding="utf-8") as f:
    text = f.read()

#分词
words = jieba.lcut(text, cut_all=False)

#停用词
stopwords = {"的", "了", "和", "是", "我", "在", "有", "就", "不", "人", "都", "一个", "也", "很", "到", "说", "要", "去", "你"}

#过滤停用词
clean_words = [w for w in words if w not in stopwords and len(w) > 1]

#统计词频
freq = Counter(clean_words)

#输出词频最高的前20个词
print("高频词:")
for word, count in freq.most_common(20):
    print(f"{word}:{count}")