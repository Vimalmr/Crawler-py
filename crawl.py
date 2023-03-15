import requests
from bs4 import BeautifulSoup

# URL of the webpage to crawl
url = 'https://kongu.ac.in'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags on the page
links = soup.find_all('a')

# Print the href attribute of each link
count,countall = 0,0 
for link in links:
    li=link.get('href')
    if li!="#": 
        print(li)
        count+=1
    countall+=1
print("No. of Crawled sites in",url,"=",count)
print("Total no.of <a> crawled:",countall)