
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Weightlifting_at_the_1976_Summer_Olympics'


#if request is successful, printing response.status_code should output '200'
s = requests.Session()
response = s.get(url, timeout=10)

#4.) parse the response content to html
soup = BeautifulSoup(response.content, 'html.parser')

#5.) Now search for the table that you need and scrape it!! THIS IS IT
medal_table = soup.find('table', {"class":"wikitable sortable plainrowheaders jquery-tablesorter"}) #this gets the 2nd table
#print(medal_table)

#6.) Return a list of rows from "medal_table" and store it in a variable
rows_all = medal_table.find_all('tr')
# row_count = len(rows_all)

