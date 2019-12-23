import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

result = requests.get(url=url)

bs_obj = BeautifulSoup(result.content, "html.parser")
lf_item = bs_obj.findAll("div", {"class":"lf_item"})
hrefs = [div.find("a")]

