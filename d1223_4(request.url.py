from urllib.request import urlopen
import json
import requests
from urllib.parse import urlparse


def get_request_url(from_date, to_date):
      url = "ttps://finance.naver.com/marketindex/worldDailyQuote.nhn?fdtc=4&marketindexCd=FX_GBPUSD&page=" + from_date + "/edate/" + to_date +"/mode/1"
      result = requests.get(urlparse(url).geturl())
      return result.json()

def call_and_print(from_date, to_date):
      json_obj = get_request_url(from_date,to_date)
      for item in json_obj['data']:
            title = item['date']
            print(title +"@" + item['op'] +"@" + item['c1'] + "@" + item['se'] + "@" + item['vo'])

from_date = "1972-01-03"
to_date = "2019-12-23"

call_and_print(from_date, to_date)


