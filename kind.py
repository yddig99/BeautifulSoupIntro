from bs4 import BeautifulSoup

# docs= '<b class="boldest">Extremely bold</b>'

# docs= '<b id="boldest">Extremely bold</b>'

# soup = BeautifulSoup( docs,'html.parser')

# tag = soup.b

# print(type(tag))

# print(tag.name)
# 
# tag.name ="blockquote"

# print(tag['id'] )

# print(tag.attrs )

# css_soup = BeautifulSoup('<p class="body"></p>','html.parser')

# print(css_soup.p['class'])

# css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')

# print(css_soup.p['class'])

#tag back to string
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>' , 'html.parser')

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)