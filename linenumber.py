from bs4 import BeautifulSoup

markup = "<p\n>Paragraph 1</p>\n   <p>Paragraph 2</p>"
# soup = BeautifulSoup(markup, 'html.parser')
soup = BeautifulSoup(markup, 'html5lib')

for tag in soup.find_all('p'):
    print(tag.sourceline,tag.sourcepos,tag.string)
