
from bs4 import BeautifulSoup
import requests
import pandas as pd
import unidecode


url = 'https://en.wikipedia.org/wiki/Weightlifting_at_the_1976_Summer_Olympics'


#if request is successful, printing response.status_code should output '200'
s = requests.Session()
response = s.get(url, timeout=10)

#4.) parse the response content to html
soup = BeautifulSoup(response.content, 'html.parser')

#5.) Now search for the table that you need and scrape it!! THIS IS IT
medal_table = soup.find('table', {"class":"wikitable sortable plainrowheaders jquery-tablesorter"}) # this gets the 2nd table

#6.) Obtain the header values and store it in an empty list   --> 'th' instead of 'tr'
headers = []
for count, header in enumerate(medal_table.find_all('th')): # what is the dimension on this thing?
    title = header.get_text(separator=',') 
    headers.append(title)
    if count == 5:
        break 

#7.) Create the dataframe AKA the house for the medal table (and add the index!)
df_medaltable = pd.DataFrame(columns=headers)

#### Current Workspace
####
#8.) Create a for loop to fill the dataframe
for tr_row in medal_table.find_all('tr'):
    print('<<row:>>', tr_row)  # this only outputs 7 - we need 11 (for 11 total rows)
    # tr_count = medal_table.find_all(tag='tr').count
    # row_data = tr_row.find_all(['td','th'])
    # for cell_data in row_data: 
    #     # get the text from each row (row_data)   
    #     # house in a variable (?)