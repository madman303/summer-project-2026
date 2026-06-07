#先爬取第一页的评论，后续再爬取其他页的评论
import requests
from bs4 import BeautifulSoup

url = "https://book.douban.com/subject/4913064/comments/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
response = requests.get(url,headers=headers)
print("状态码:",response.status_code)
soup = BeautifulSoup(response.text,"html.parser")
comments = soup.find_all("span",class_="short")

for c in comments:
    print(c.text.strip())

import json
comments_list = []
for c in comments:
    comments_list.append(c.text.strip())
    with open("comments.json","w",encoding="utf-8") as f:
        json.dump(comments_list,f,ensure_ascii=False,indent=2)

print(f"已保存{len(comments_list)}条评论")