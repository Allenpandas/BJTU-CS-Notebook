import requests
import re
import time
payload = ""
# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cookie": "l=AurqcPuigwQdnQv7WvAfCoR1OlrRQW7h; isg=BHp6mNB79CHqYXpVEiRteXyyyKNcg8YEwjgLqoRvCI3ddxqxbLtOFUBGwwOrZ3ad; thw=cn; cna=VsJQERAypn0CATrXFEIahcz8; t=0eed37629fe7ef5ec0b8ecb6cd3a3577; tracknick=tb830309_22; _cc_=UtASsssmfA%3D%3D; tg=0; ubn=p; ucn=unzbyun; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=981798063989731689; hng=CN%7Czh-CN%7CCNY%7C156; um=0712F33290AB8A6D01951C8161A2DF2CDC7C5278664EE3E02F8F6195B27229B88A7470FD7B89F7FACD43AD3E795C914CC2A8BEB1FA88729A3A74257D8EE4FBBC; enc=1UeyOeN0l7Fkx0yPu7l6BuiPkT%2BdSxE0EqUM26jcSMdi1LtYaZbjQCMj5dKU3P0qfGwJn8QqYXc6oJugH%2FhFRA%3D%3D; ali_ab=58.215.20.66.1516409089271.6; mt=ci%3D-1_1; cookie2=104f8fc9c13eb24c296768a50cabdd6e; _tb_token_=ee7e1e1e7dbe7; v=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;` rv:47.0) Gecko/20100101 Firefox/47.0"
}


# 获得文章列表urls
def getUrls(url):
    # 发送请求
    resp = requests.request("GET", url, data=payload, headers=headers)
    # 设置解码方式
    resp.encoding=resp.apparent_encoding
    # 这里会用设置的解码方式解码
    html_source = resp.text
    # 正则表达式，取出网页中的url链接（一些寻找注入点的工具也是这么做出来的）
    urls = re.findall("https://[^>\";\']*\d", html_source)
    new_urls = []
    for url in urls:
        if 'details' in url:
            if url not in new_urls:
                new_urls.append(url)
    return new_urls


# 机器学习算法面试题汇总
url1 = "https://blog.csdn.net/m0_38068876/article/details/122746782"

urls = getUrls(url1)
while True:
    for url in urls:
        requests.request("GET", url, data=payload, headers=headers)
        print(url, "Ok")
        time.sleep(10)
    time.sleep(30)
