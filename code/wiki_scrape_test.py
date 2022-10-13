#import mods
import requests
from bs4 import BeautifulSoup

#Request page from the specified url
page = requests.get('https://en.wikipedia.org/wiki/Weightlifting_at_the_1976_Summer_Olympics')


#scrape webpage with BeautifulSoup <3
soup = BeautifulSoup(page.content, 'html.parser')
list(soup.children) # --> because 'children' returns a list generator

### Now I want to find occurrences of something in the HTML w/ 'find_all()' method? What other methods at our disposal?