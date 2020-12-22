import requests
from bs4 import BeautifulSoup
import json

'''
Example:1

url='https://www.facebook.com'

res=requests.get(url).content

soup=BeautifulSoup(res,'lxml')
#print(soup.prettify())

print(soup.a.text)

print(soup.title.text)

End...
'''

'''
Exmaple:2

url='https://www.indiatoday.in/'

res=requests.get(url).content

soup=BeautifulSoup(res,'lxml')

#print(soup.prettify())

a_tag=soup.find_all('a')
print(a_tag)

for h3_tag in soup.find_all('h3'):
    for a_tag in h3_tag.find_all('a'):
        print("Title:",a_tag.text)
        print("Website:",url+a_tag.get('href'))

End     
'''
#url='https://www.flipkart.com/pandas-everyone-python-data-analysis-1e/p/itmf52kpyy4umgud?pid=9789352869169&lid=LSTBOK97893528691697DQGK7&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=fa61709d-eb5b-490e-b69c-3dc97f8310b5.9789352869169.SEARCH&ppt=sp&ppn=sp&ssid=v0i8cj3h9c0000001578206793779&qH=4dee1b2351862003'
#url='https://www.flipkart.com/data-science-scratch-first-principles-python-2nd/p/itm14ad5c0033c2a?pid=9789352138326&lid=LSTBOK9789352138326X9WQFK&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=46d635f2-7e01-4aec-ade2-de94b1c5feb4.9789352138326.SEARCH&ppt=sp&ppn=sp&ssid=v0i8cj3h9c0000001578206793779&qH=4dee1b2351862003'
url='https://www.flipkart.com/introduction-computation-programming-using-python-application-understanding-data/p/itmeztj89eghagzm?pid=9788120352926&lid=LSTBOK9788120352926HNSG3J&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=f36f8ce8-a3e4-4c2a-bf1a-513d87198967.9788120352926.SEARCH&ppt=sp&ppn=sp&ssid=v0i8cj3h9c0000001578206793779&qH=4dee1b2351862003'

res=requests.get(url).content

soup=BeautifulSoup(res,'lxml')

title=soup.find('span',class_='_35KyD6')
print("Title:",title.text)

price=soup.find('div',class_='_1vC4OE _3qQ9m1')
print("price:",price.text)

data=soup.find('script',id='jsonLD').text
#print(data)

context=json.loads(data)
#print(context)

#print((context[0]))



#print("Title:",context[0]['name'])
print("Rating:",context[0]['aggregateRating']['ratingValue'])
print("Review_Count:",context[0]['aggregateRating']['reviewCount'])

#print("Author Name:",context[0]['author'][0]['name'])
#print("BookFormat:",context[0]['bookFormat'])
#print("Reviews:",soup.find('span',class_='_38sUEc').text)
#print("Ratings:",soup.find('span',id='productRating_LSTBOK97893528691697DQGK7_9789352869169_').text)
# print("Price:",context[0]['workExample'][0]['potentialAction']['expectsAcceptanceOf']['price'])