"""A python web scraper for searching Amazon"""

import os
import csv

from bs4 import BeautifulSoup
from selenium import webdriver

import helpers

# Get Query from User
query = helpers.get_query()

# Setup webdriver using Google Chrome
chromedriver = os.environ.get("CHROMEDRIVER")
driver = webdriver.Chrome(chromedriver)

# Search 20 pages
records = []
for page in range(1, 21):
    # Open page
    url = helpers.create_url(query, str(page))
    driver.get(url)

    # Extract page data
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    # Extract records from data
    page_records = list(filter(None, [helpers.extract_item_data(item) for item in results]))
    records.extend(page_records)

# Close page
driver.close()

# Save records to CSV file
with open(f'Search_{query}.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    [writer.writerow(data) for data in records]