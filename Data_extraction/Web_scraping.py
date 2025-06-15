"""
Why web scraping?
- lets you extract data from websites that don't have an API. Powerful when you want real-time data on:
News Articles, stock prices, job listings, product reviews, sports stats

Using requests + beautifulsoup
Requests: fetch web pages
BeautifulSoup: parse html content
pandas: organize data
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# step 1: send a request
url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# step 2: find book containers
books = soup.find_all('article', class_= 'product_pod')

# step 3: Extract info
book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()
    rating = book.p['class'][1]  # class = 'star-rating Three'
    
    book_data.append({
        'Title': title,
        'Price': price,
        'Rating': rating
    })


# step 4: Convert to dataframe
df = pd.DataFrame(book_data)
print(df.head())
print(df)
