from bs4 import BeautifulSoup
import copy


markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup = BeautifulSoup(markup, 'html.parser')

p_copy = copy.copy(soup.p)

print (p_copy)