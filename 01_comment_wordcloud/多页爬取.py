#爬取多页内容，先使用for循环试试
import requests
from bs4 import BeautifulSoup
import json
import time 

#先随便抓取几页
total_pages = 5

    
url = "https://book.douban.com/subject/4913064/comments/"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Cookie": "bid=NRo2qseLa8s; _pk_id.100001.3ac3=7c978ffce6b45018.1778513753.; __utma=30149280.1877231581.1778513754.1780557584.1780583665.18; __utmz=30149280.1780330239.13.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=81379588.408423591.1778513754.1780557584.1780583665.17; __utmz=81379588.1780476227.13.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; viewed=\"4913064\"; _vwo_uuid_v2=DA54B07A1B7E22B56FDC94AC548359AE9|19ca0cf3ffafcca3549a16072b3549b9; __yadk_uid=000XeuYY4awXE4llBIhH6EIfE6Xu3pBm; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1780583664%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%E6%B4%BB%E7%9D%80%22%5D; ll=\"118348\"; ap_v=0,6.0; _pk_ses.100001.3ac3=1; __utmb=30149280.8.10.1780583665; __utmc=30149280; __utmt_douban=1; __utmb=81379588.8.10.1780583665; __utmc=81379588; __utmt=1; dbcl2=\"295423784:kQs9KF1CExk\"; ck=dIsx; frodotk_db=\"1987a3ccca169c4c4c96eb665e43d4e4\"; push_noty_num=0; push_doumail_num=0"
}

#创建一个空表格来存储评论
all_comments = []

#数量少，先使用for循环来爬取评论,当爬取数量足够多的时候，可以考虑使用多线程或者异步来加速爬取，其实可以尝试一下递归，不过递归可能会有深度限制的问题
for page in range(total_pages):
    start = page * 20
    params = {"start": start, "limit": 20}
    
    response = requests.get(url,headers=headers,params=params)
    print(f"第{page + 1}页 状态码: {response.status_code}")

    #每次请求后休息1秒，避免过于频繁的请求导致被封禁
    time.sleep(1)
    
    soup = BeautifulSoup(response.text,"html.parser")
    comments = soup.find_all("span",class_="short")
    print(f"第{page + 1}页 找到{len(comments)}条评论")


    for c in comments:
        all_comments.append(c.text.strip())
with open("comments.json","w",encoding="utf-8") as f:
    json.dump(all_comments,f,ensure_ascii=False,indent=2)

print(f"已保存{len(all_comments)}条评论")