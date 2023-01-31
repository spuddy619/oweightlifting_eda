
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
medal_table = soup.find('table', {"class":"wikitable sortable plainrowheaders jquery-tablesorter"}) #this gets the 2nd table
# print(medal_table)

#6.) Obtain the header values and store it in an empty list   --> 'th' instead of 'tr'
headers = []
for count, header in enumerate(medal_table.find_all('th')): # what is the dimension on this thing?
    title = header.get_text(separator=',') 
    headers.append(title)
    if count == 5:
        break 

#7.) Create the dataframe AKA the house for the medal table!
df_medaltable = pd.DataFrame(columns=headers)

#8.) Create a for loop to fill the dataframe -- employ the loc[]method to add row data to df_medaltable
for tr_row in medal_table.find_all('tr')[1:]:
    row_data = tr_row.find_all(['td','th'])
    i = 0
    for cell_data in row_data:
        i+=1
        row=[] # on each loop we empty 'row' to accept this iterations cell data 
        cell_text = cell_data.get_text() #do we need arguments here?
        cell_text = unidecode.unidecode(cell_text)  # gets rid of the non-ASCII characters
        row.append(cell_text)
        df_medaltable.loc[i] = row
        if i == 8:
            break
        

#         length = len(df_medaltable)
#         df_medaltable.loc[length] = row       

# print(df_medaltable.head(10))


################################

# ################################
# #7.) Create a dataframe: set up the dataframe to house our medal table
# df_medaltable = pd.DataFrame(columns = headers)

# row_text=[]
# #7.) Create a for loop to extract the data we want and fill into our new dataframe
# for x in medal_table.find_all('tr')[1:]:
#     row_data = x.find_all(['td','th']) # or x.find_all('tr')
#     row = [i.text for i in row_data]
#     length = len(df_medaltable)
#     df_medaltable.loc[length] = row

# ### Reference for the for loop
# # Create a for loop to fill mydata
# # for j in table1.find_all(‘tr’)[1:]:
# #  row_data = j.find_all(‘td’)
# #  row = [i.text for i in row_data]
# #  length = len(mydata)
# #  mydata.loc[length] = row
# #  ###
# #8 Make the dataframe with our newly scraped table data and the list of columns that we created earlier 
# # df_medaltable = pd.DataFrame(row_text,columns=headers)

# # #9.) Get our rows from 'medal_table':
# # rows = medal_table.find_all('tr')
# # row_text = []
# # for row in rows: 
# #     row_data = row.find_all('th')
# #     for row_raw in row_data:
# #         row_text.append(row_raw.get_text(strip=True, separator = ", "))
        

        
    
# # #8.) Get dimensions of the medal table, save in variable s
# # row_count = len(rows_all)
# # col_count = 6 # should remain the same across all URLs right?

# # #9.) Initialize an adequate number of variables and create list of all the rows
# # row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11 = ([] for i in range(row_count))  #initializes multiple variables to hold the row data for each row
# # rows = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11]

# # #10.) Now we use a for loop to extract the data we want
# # for i, row in enumerate(rows_all):
# #     rows[i] = row.get_text(strip=True, separator =", ")  


# # #10.) Now we make our dataframe of the medal table while making sure to set the header
# # # headers=['Rank', 'Nation', 'Gold', 'Silver', 'Bronze', 'Total']
# # df_medal_table = pd.DataFrame(
# #     {'Rank': row1,
# #     'Nation': row2,
# #     }
# # )
    
    
