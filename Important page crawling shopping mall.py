import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://jolse.com/category/toners-mists/1019/"
result = requests.get(url, headers=headers)
bs_obj = BeautifulSoup(result.text, features="lxml")

ul = bs_obj.find("ul", {"class":"prdList grid4"})
boxes = ul.findAll("div", {"class":"box"})
for box in boxes:
    p_tag = box.find("p", {"class":"name"})
    span = p_tag.find("span")
    print(span.text) #화장품 이름 출력

def get_product_info(box):
    ptag = box.find("p", {"class":"name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")
    name = spans_name[0].text
    price = spans_price[1].text
    print(price)

    return {"name": name, "price": price}

for box in boxes:
    product_info = get_product_info(box)
    # print(product_info) #화장품 원래 가격 추출

def get_product_info(box):
    ptag = box.find("p", {"class":"name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")
    name = spans_name[0].text
    price = spans_price[1].text
    atag = box.find("a")
    link = atag['href']
    print(price)

    return {"name":name, "price": price, "link":link}

for box in boxes:
    product_info = get_product_info(box)
    print(product_info)





