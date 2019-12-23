import requests
from urllib.parse import urlparse

keyword = "광운대"
def get_api_result(keyword, display,start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
    + "&display=" + str(display) \
    + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id":"j9ZfrSBb7iidQl18hfvN",
                                   "X-Naver-Client-Secret":"hzpGoUtfBh"})
    return result.json()
json_obj = get_api_result("광운대학교", 100, 101)
print(json_obj)

# json_obj = result.json()
for item in json_obj['items']:
    print("Title: " + item['title'].replace("<b>","").replace("</b>",""),
          "Link: " + item["link"])
# # print("display :"+str(json_obj['display']))
# # # print("start :"+str(json_obj['start']))
# # # print("items :"+str(len(json_obj['items'])))
# print(json_obj)