####import packages for code reading
import requests
from bs4 import BeautifulSoup
import pandas as pd

####request data from page
page = requests.get('https://www.healthline.com/health-news')
page

## bs4 objects being created
soup = BeautifulSoup(page.text, 'html.parser')
soup

##formatting and cleaning data from website
print(soup.prettify())

##pulling a specific tab in the website and making it human readable
conditions = soup.find_all('a', tabindex="-1")
output_conditions = []

for i in conditions:
    print(i.text)
    output_conditions.append(i.text)

len(conditions) ##number of items under the above tab


articles = soup.find_all('ol', class_='css-1iruc8t')
output_articles = []

for i in articles:
    print(i.text)
    output_articles.append(i.text)

len(articles)







































