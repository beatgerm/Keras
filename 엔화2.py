import requests
from bs4 import BeautifulSoup
i = 1
numbers = []
url = "https://finance.naver.com/marketindex/worldDailyQuote.nhn?fdtc=4&marketindexCd=FX_USDJPY&page=" + str(i)
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
section_exchange = bs_obj.find("table", {"class": "tbl_exchange today"})
tr_tag = section_exchange.findAll("tr")



for index, table_rows in enumerate(tr_tag):
    if index > 0:
        td_tag = tr_tag.findAll("td")
        date = td_tag.text.strip()
        print(date.text)

for index, table_rows in enumerate(tr_tag):
    if index > 0:
        num = td_tag.text.strip()
        print(num.text)


'''
    for index, table_rows in enumerate(td_tag_num):
        if index > 0:
            num = td_tag_num.strip()
            print(num)

    return {"date": date, "num": num}

for i in range(1, 1100):
    get_exchange_info("https://finance.naver.com/marketindex/worldDailyQuote.nhn?fdtc=4&marketindexCd=FX_USDJPY&page=" + str(i))

'''











