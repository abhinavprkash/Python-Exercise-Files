import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

n = 0
count = 0

url = 'http://py4e-data.dr-chuck.net/known_by_Alyse.html'
#url = input("Enter URL:")

numbers = int(input("Enter count:"))
position = int(input("Enter position:"))

while n < numbers:  # <----- there's your variable of how many times to try
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
      count = count + 1
      if count == position:  # <------- and the variable to get the position
         url = tag.get('href', None)
         print("Retrieving:", url)
         count = 0
         break
    n = n + 1
