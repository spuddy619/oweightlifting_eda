### This block of code is dedicated to scraping and storing a list of all the pertinent URLs for Weightlifting in the Summer Olympics ###

from bs4 import BeautifulSoup
import requests

#1.) Set URL variable - a URL with links to all the other pertinent Weightlifting at the Summer Olympics links
url_origin= 'https://en.wikipedia.org/wiki/Weightlifting_at_the_1976_Summer_Olympics'

#2.) Get request for URL
s = requests.Session()
response = s.get(url_origin, timeout=10)

#3.) parse the response content to html so we can work with it~
soup = BeautifulSoup(response.content, 'html.parser') 

#4.) In preparation of the url retrieval, lets have a variable to house the retrieved data in!
url_home = [url_origin]

#5.) Scrape the URL and use find_all to discover all the other URLs 
# We are going to turn the information we want into an accessible, list form via "find_all" 
url_data = soup.find_all("td", {"colspan":"2", "class":"navbox-list navbox-odd hlist", "style":"width:100%;padding:0"}) 
(url_data[1]) # this prints out the 2nd <td> tag with {"colspan":"2", "class":"navbox-list navbox-odd hlist", "style":"width:100%;padding:0"} which is the one we want

#6.) Lets loop through the chunk of data we extracted (url_data) and perform actions that will a.) take out the pertinent links and then b.) store it in our url_home
url_prefix = 'https://en.wikipedia.org'
i = 0
for link in url_data[1].find_all("a"):
    i += 1
    url_suffix = link.get('href')
    if isinstance(url_suffix, str) == True:         #eliminate the first couple entries as they are before 1976 Olympics
        url_full = url_prefix + url_suffix
    if i >16 and i<28:  #to limit the URL additions to the pertinent Summer Olympics we desire () -- Pinpoint the specific window of time that we want
        url_home.append(url_full)
print(url_home)

