import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
print(ul)
#<ul>
# <li>hello</li>
# <li>bye</li>
# <li>welcome</li>
# </ul>

li = ul.find("li")
print(li.text)
# hello

li = ul.find("li")
print(li)
#<li>hello</li>

ul = bs_obj.find("ul")
lis = ul.findAll("li")
print(lis)
#[<li>hello</li>, <li>bye</li>, <li>welcome</li>]

ul = bs_obj.find("ul")
lis = ul.findAll("li")
print(lis[1])
#<li>bye</li>

ul = bs_obj.find("ul")
lis = ul.findAll("li")
print(lis[2])
#<li>welcome</li>


