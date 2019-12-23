from urllib.request import urlopen
import json
import requests
from urllib.parse import urlparse

from_date = "2019-01-01"
to_date = "2019-12-23"
def get_request_url(from_date, to_date):
      url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2019-12-23" + from_date + "/edate/" + to_date +"/mode/1"
      result = requests.get(urlparse(url).geturl())
      return result.json()

def call_and_print(from_date, to_date):
      json_obj = get_request_url(from_date,to_date)
      for item in json_obj['data']:
            title = item['date']
            title1 = item['settlement']
            print(title +"@"+ title1)


call_and_print(from_date, to_date)
