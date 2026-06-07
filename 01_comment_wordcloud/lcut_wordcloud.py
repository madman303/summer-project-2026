import jieba
from collections import Counter
from generate_wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("comments.txt","r",encoding="utf-8") as f:
    text = f.read()

words = jieba.lcut(text)

stopwords = {"的","了","和","是","我","在","有","就","不","人","都","一个","也","很","到","说","要","去","你"}

cleaned_words = [w for w in words if w not in stopwords and len(w) > 1]

freq = Counter(cleaned_words)

wordcloud = WordCloud(
    font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    width=800,
    height=600,
    background_color="white",
    max_words=100
).generate_from_frequencies(freq)

plt.figure(figsize=(10,8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.savefig("wordcloud.png")
plt.show()

print("词云图已生成，保存为 wordcloud.png")