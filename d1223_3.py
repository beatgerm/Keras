import requests
from urllib.parse import urlparse

keyword = "광운대"
def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword \
    + "&display=" + str(display) \
    + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id":"j9ZfrSBb7iidQl18hfvN",
                                   "X-Naver-Client-Secret":"hzpGoUtfBh"})
    return result.json()
def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>","").replace("<b>","")
        print(title + "@" + item['bloggername'] + "@" + item['link'])
keyword = "광운대"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)