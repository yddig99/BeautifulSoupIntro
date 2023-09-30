from bs4 import BeautifulSoup

markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup = BeautifulSoup(markup, 'html.parser')
first_b, second_b = soup.find_all('b')
# print (first_b == second_b)

print(first_b is second_b)