import json
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import jieba
from collections import Counter

with open("comments.txt","r",encoding="utf-8") as f:
    text = f.read()

words = jieba.lcut(text,cut_all=False)

stopwords = {"的","了","和","是","我","在","有","就","不","人","都","一个","也","很","到","说","要","去","你"}

clean_words = [w for w in words if w not in stopwords and len(w) > 1]
freq = Counter(clean_words)

wordcloud = WordCloud(
    font_path="/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    width=800,
    height=600,
    background_color="white",
    max_words=100
).generate_from_frequencies(freq)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("wordcloud.png",dpi=300)
plt.show()

print("词云图已保存为wordcloud.png")