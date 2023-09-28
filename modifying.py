from bs4 import BeautifulSoup

# soup = BeautifulSoup('<b class ="boldest">Extremely bold</b>' ,'html.parser')
# tag = soup.b
# tag.name ="blockquote"
# tag['class']= 'verybold'
# tag['id']=1
# print(tag)

#modifyng a string
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup ,'html.parser')
# tag=soup.a
# print(tag)
# tag.string="gideon kwake is a hacker"
# print(tag)

#append a tag
# soup = BeautifulSoup("<a>Gideon</a>" ,"html.parser")
# soup.a.append("Kwake")
# print(soup)
# print(soup.a.contents)

#extend() contents
# soup = BeautifulSoup("<a>Gideon</a>" ,"html.parser")
# soup.a.extend(["Kwake","Makau"])
# print(soup.a.contents)


#append new string with navigableString()
# soup = BeautifulSoup("<b></b>","html.parser")
# tag= soup.b
# tag.append(" Gideonis very healthy")
# New_string= NavigableString(" Gideon is also Wealthy")
# tag.append(New_string)
# print(tag)


#insert into contents
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup ,"html.parser")
# tag = soup.a
# tag.insert(1, "but did not endorse ")
# print(tag)


#insert before and after
soup = BeautifulSoup("<b>stop</b>","html.parser")
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_before(tag)
print(soup.b)



