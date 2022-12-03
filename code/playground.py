from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

s = requests.Session()
response = s.get(url, timeout=10)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

#Find All Tables
all_tables=soup.find_all('table') # this produces a LIST of elements; not a singular entity
#Find the table we need
right_table = soup.find('table', {"class":'wikitable sortable'})
print(right_table.prettify())
