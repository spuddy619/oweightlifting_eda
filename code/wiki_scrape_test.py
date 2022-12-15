# import required modules
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Weightlifting_at_the_1976_Summer_Olympics'
#requests.get() vs requests.Session() 


#create session object - persistent parameters across all html requests
    #if request is successful, printing response.status_code should output '200'
s = requests.Session()
response = s.get(url, timeout=10)
# print(response.status_code)

#parse response content to html
soup = BeautifulSoup(response.content, 'html.parser')
# to view the content, now in html format
pretty_soup = soup.prettify()

# # Prints the title of the wikipedia page
# print(soup.title.string)

# find all the tables in page and gather them  --> I believe this finds all the tags that say 'table'
all_tables = soup.find_all('table')

# Now search for the table that you need and scrape it!! THIS IS IT
medal_table = soup.find('table', {"class":"wikitable sortable plainrowheaders jquery-tablesorter"}) #this gets the 2nd table

# This finds ALL the rows from the table "medal_table"
rows_all = medal_table.find_all('tr')
row_count = len(rows_all)

# #This finds the FIRST row from the table AKA the header row
row_1 = medal_table.find('tr')


#Count the number of columns
col_count = len(row_1)

#Get Table Header Attributes
header_attributes = (row_1.find_all(text=True)) #This is the text values for the HEADER ROW

#Now I want each row's text as a list (so we can build the table)
#store each row into variables

row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11 = ([] for i in range(11))  #initializes multiple variables to hold the row data for each row
rows = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11]
for i, row in enumerate(rows_all): # I am using enumerate here so I have 2 counting methods for the two lock scrolls (lists) here
    rows[i] = row.get_text(strip=True, separator =", ")  # strips out unicode('\xa0') and has separator of comma + space

#time to build the dataframe now as we now have our ingredients.
    #put a list of lists into pd.DataFrame() ? 


### testing space here ###
##########################

deefer = pd.DataFrame(rows)
print(deefer)

# pandas, numpy, BeautifulSoup, 