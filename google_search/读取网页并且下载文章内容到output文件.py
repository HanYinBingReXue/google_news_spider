import requests
import base64

# from pprint import pprint
from bs4 import BeautifulSoup
import ssl

from GoogleNews import GoogleNews
from pprint import pprint

googlenews = GoogleNews()
# print(googlenews.getVersion())
googlenews.enableException(True)
googlenews.set_lang("en")
googlenews.set_encode("utf-8")
# googlenews.set_period('7d')

# ================================================================================
googlenews.set_time_range("01/01/2022", "02/28/2023")
# 输入关键词
googlenews.get_news("distressed inventory wayfair")
# ================================================================================
# pprint(googlenews.results())
# pprint(googlenews.get_links())
# 获得所有link
links = googlenews.get_links()
for each in links[:20]:
    print("获取链接成功:", each)
    each = each.split("/")
    del each[1]
    encodedcontent = each[-1].split("?")[0]
    # print(encodedcontent, len(encodedcontent))
    while len(encodedcontent) % 4 != 0:
        encodedcontent += "="
    # print(encodedcontent, len(encodedcontent))
    print("获取加密网址成功:", encodedcontent)
    # Decode the string
    decoded_string = base64.urlsafe_b64decode(encodedcontent).decode("utf-8", errors="replace")
    start = decoded_string.index("https")
    end = decoded_string.index("�", start)
    link = decoded_string[start:end]
    print("解码网址成功:", link)

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36,Gecko/20100101 Firefox/66.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
    }
    strhtml = requests.get(link, headers=headers)  # Get方式获取网页数据
    soup = BeautifulSoup(strhtml.content, "html.parser")

    text_elements = soup.find_all("p")
    # pprint(text_elements)
    with open("output.text", "a+") as f:
        for element in text_elements:
            # pprint(element.get_text())
            f.write(element.get_text())
    f.close()
print("文件录入结束！")
