import json

#读取文件
with open("comments.json","r",encoding="utf-8") as f:
    comments = json.load(f)

#把评论写入txt文件
with open("comments.txt","w",encoding="utf-8") as f:
    for comment in comments:
        f.write(comment + "\n")
print("已写入评论")