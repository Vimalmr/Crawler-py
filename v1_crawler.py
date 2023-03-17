#crawler V.1
import time
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

# Set the number of links to crawl
num_links_to_crawl = 100

# Set the user agent to use for the request
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

# Set the headers for the request
headers = {'User-Agent': user_agent}

# Initialize the controller for the Tor network
with Controller.from_port(port=9051) as controller:
    # Set the controller password
    controller.authenticate(password='16:8B8D9633F9BEE99B606867BC7B4152FBF8154700669969E4F40AD2C193') #that hash is "vimal"

url = input("Enter Your Onion Url: ")

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
