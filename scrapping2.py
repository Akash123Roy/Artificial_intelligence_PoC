import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Specify the URL
url = 'https://www.example.com/jobs'  # Replace with a valid job listings page

# Step 2: Send an HTTP request to the URL
response = requests.get(url)

# Step 3: Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 4: Extract all job postings
job_listings = soup.find_all('div', class_='job-post')

# Step 5: Loop through each job and extract information
data = []
for job in job_listings:
    title = job.find('h2', class_='job-title').text.strip()
    company = job.find('div', class_='company-name').text.strip()
    location = job.find('div', class_='job-location').text.strip()
    link = job.find('a', class_='apply-link')['href']
    
    data.append({
        'Title': title,
        'Company': company,
        'Location': location,
        'Link': link
    })

# Step 6: Store data in a Pandas DataFrame
df = pd.DataFrame(data)

# Step 7: Save the data to a CSV file
df.to_csv('job_listings.csv', index=False)
print("Data saved to job_listings.csv")
