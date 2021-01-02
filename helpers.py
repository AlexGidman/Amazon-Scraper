"""Helper functions for scraper.py"""

from bs4 import BeautifulSoup, element

def get_query() -> str:
    """Get query string from user"""
    query = input("Enter Query: ")
    return query.replace(" ", "+")
   

def create_url(query: str, page: str) -> str:
    """Create URL to search Amazon"""
    return f'https://www.amazon.co.uk/s?k={query}&page={page}'


def extract_item_data(item: element.Tag) -> dict:
    "Extracts useful item data and returns as a dict"
    # <a> element
    atag = item.h2.a

    description = atag.text.strip()
    url = f"https://www.amazon.co.uk{atag.get('href')}"

    try:
        price = item.find('span', 'a-price').find('span', 'a-offscreen').text
    except AttributeError:
        return
    
    try:
        rating = float(item.i.text[:3])
    except Exception:
        rating = ''
    
    img_url = item.find('span', {'data-component-type': 's-product-image'}).findChildren('img')[0]['src']
    
    return {
        'description': description,
        'url': url,
        'price': price,
        'rating': rating,
        'img_url': img_url
    }