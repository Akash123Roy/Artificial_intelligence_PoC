import requests
from bs4 import BeautifulSoup

# Step 1: Specify the URL
url = 'https://www.covid19india.org/'  # Example blog

# Step 2: Send an HTTP request to the URL
response = requests.get(url)

# Step 3: Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 4: Extract all article titles and their links
articles = soup.find_all('article')
for article in articles:
    title = article.find('h2').text
    link = article.find('a').get('href')
    print(f'Title: {title}\nLink: {link}\n')
