项目计划书：用户评论情感词云
一、项目概述
项目名称	豆瓣《活着》短评爬取与词云分析
项目编号	01_comment_wordcloud
开发环境	Debian Linux + Python 3
目标网站	https://book.douban.com/subject/1085798/comments/

核心功能	爬取豆瓣《活着》短评，生成中文词云
二、技术栈
工具库	用途
python3	主编程语言
requests	发送HTTP请求
BeautifulSoup4 你	解析HTML页面
jieba	中文分词
wordcloud	生成词云图
matplotlib	显示/保存词云图
pandas	数据存储与处理
三、项目结构
summer-project-2025/
├── 01_comment_wordcloud/
│   ├── crawl_comments.py      # 爬虫代码
│   ├── comments.json          # 爬取的原始评论数据
│   ├── comments.csv           # 评论数据表格
│   ├── wordcloud_generator.py # 词云生成代码
│   ├── wordcloud.png          # 生成的词云图
│   └── stopwords.txt          # 停用词表（可选）
├── notes/
│   └── 01_page_structure.png  # HTML结构截图
├── requirements.txt           # Python依赖列表
└── README.md                  # 项目说明
四、环境搭建步骤
4.1系统环境（Debian）
4.2创建虚拟环境并安装依赖
4.3生成requirements.txt
五、爬虫代码实现
5.1爬取评论
5.2生成词云
六、运行说明
6.1运行爬虫
6.2生成词云
七、注意事项（避坑指南）
问题	原因	解决方法
返回418	反爬虫拦截	必须携带完整的Cookie,添加User-Agent
评论抓不到	HTML结构变化	同时适配.short和.comment-content
中文显示方块	字体不支持中文	制定中文字体路径
jieba分词不准确	默认词典	可添加自定义词典或调整cut_all参数
请求被封IP	请求频率过高	每次请求后time.sleep(2)

八、Cookie获取方法
用浏览器打开豆瓣并登录
•	按 F12 → Network 标签
•	刷新页面，点击任意请求
•	找到 Request Headers 中的 Cookie:
•	复制整段内容（从 bid= 开始到末尾

当爬取数量较少的时候，先使用for循环，当爬取数量较多的时候可以考虑使用多线程或者异步来加速爬取，其实也可以尝试一下递归，但是使用递归可能会出现深度限制的问题
注意：
不要并发（多线程）：如果同时发起多个请求将会瞬间触发反爬
Cookie需要定期更新
