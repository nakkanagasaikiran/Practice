from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = ('https://www.investing.com/equities/trending-stocks/')
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")

title = page_soup.find("title")
print(title)

