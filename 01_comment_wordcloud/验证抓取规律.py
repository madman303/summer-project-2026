# 验证一下，看看能不能爬取第二页的评论内容
import requests
from bs4 import BeautifulSoup

url = "https://book.douban.com/subject/4913064/comments/"
params = {"start": 0, "limit": 20}
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Cookie": "bid=NRo2qseLa8s; _pk_id.100001.3ac3=7c978ffce6b45018.1778513753.; __utma=30149280.1877231581.1778513754.1780557584.1780583665.18; __utmz=30149280.1780330239.13.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=81379588.408423591.1778513754.1780557584.1780583665.17; __utmz=81379588.1780476227.13.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; viewed=\"4913064\"; _vwo_uuid_v2=DA54B07A1B7E22B56FDC94AC548359AE9|19ca0cf3ffafcca3549a16072b3549b9; __yadk_uid=000XeuYY4awXE4llBIhH6EIfE6Xu3pBm; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1780583664%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%E6%B4%BB%E7%9D%80%22%5D; ll=\"118348\"; ap_v=0,6.0; _pk_ses.100001.3ac3=1; __utmb=30149280.8.10.1780583665; __utmc=30149280; __utmt_douban=1; __utmb=81379588.8.10.1780583665; __utmc=81379588; __utmt=1; dbcl2=\"295423784:kQs9KF1CExk\"; ck=dIsx; frodotk_db=\"1987a3ccca169c4c4c96eb665e43d4e4\"; push_noty_num=0; push_doumail_num=0"
}

response = requests.get(url,headers=headers,params=params)
print("状态码:",response.status_code)
soup = BeautifulSoup(response.text,"html.parser")
comments = soup.find_all("span",class_="short")

print(f"找到{len(comments)}条评论")

if comments:
    print(comments[0].text.strip())