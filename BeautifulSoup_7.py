import urllib.request
import bs4

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"mlist2 no_bg"})
lis = ul.findAll("li")


for li in lis:
    a_tag = li.find("a")
    strong = a_tag.find("strong")
    print(strong.text)