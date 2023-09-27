html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.find_all('b'))

#regular expression find all t in the text
# for tag in soup.find_all(re.compile("t")):
#     print(tag.name)

#find all a and b tags
# print(soup.find_all(["a", "b"]))

#finds all tags
# for tag in soup.find_all(True):
#     print(tag.name)

#finding class tags only exepting tags with id
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# print(soup.find_all(has_class_but_no_id))

#filter a specific tag
def not_lacie(href):
    return href and not re.compile("lacie").search(href)
print(soup.find_all(href=not_lacie))