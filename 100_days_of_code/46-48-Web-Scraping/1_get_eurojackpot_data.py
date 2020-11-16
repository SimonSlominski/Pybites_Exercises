from requests import get
from bs4 import BeautifulSoup
import pandas as pd


# Select the website URL to scrap
URL = 'https://www.wynikilotto.net.pl/eurojackpot/wyniki/500/'
site = get(URL)
site.raise_for_status()

# Beautiful Soup — HTML Parser
soup = BeautifulSoup(site.text, 'html.parser')

# Select data from the website URL and add them to the list
stable = soup.find('table', attrs={'class':'tabela'})
# print(stable)

# # The <tr> tag defines a row in an HTML table
all_tr = stable.find_all('tr')
# print(all_tr)

# Initialise an empty list for data
data = []
#
# # The <td> tag defines a standard data cell in an HTML table
for td in all_tr:
    columns = td.find_all('td')
    columns = [td.text.strip()
               for td in columns]
    data.append([td
                 for td in columns
                 if td])

# Export scraped data to a CSV file
df_lotto = pd.DataFrame(data)
df_lotto.to_csv('eurojackpot_data.csv')
