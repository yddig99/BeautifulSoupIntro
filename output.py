from bs4 import  BeautifulSoup

markup = BeautifulSoup('<a href="http://example.com/">I linked to <i>example.com</i></a>','html.parser')
# print(markup.prettify(formatter="minimal")) 
# print(markup.a.prettify())
# print(str(markup)) no fancy formmating
# print(markup.i)
