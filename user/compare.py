import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def scrape_google_shopping(product: str) -> pd.DataFrame | None:
    """
    Scrapes Google Shopping results for a given product.

    Args:
        product: The name of the product to search for.

    Returns:
        A pandas DataFrame containing the product's name, price, seller, image, and link,
        or None if no results are found or scraping fails.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept-Language': 'en-IN,en;q=0.5'
    }
    
    params = {
        'q': product,
        'tbm': 'shop',
        'hl': 'en',
    }

    try:
        response = requests.get('https://www.google.com/search', params=params, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch Google Shopping page. Error: {e}")
        return None

    soup = bs(response.content.decode('utf-8'), 'html.parser')
    
    results = []
    
    for card in soup.find_all('div', class_='sh-dgr__content'):
        result = {}
        try:
            result['price'] = card.find('span', class_='OFFNJ').text
            
            link_element = card.find('a', class_='xCpuod')
            if link_element and 'href' in link_element.attrs:
                result['link'] = link_element['href'].replace('/url?url=', '')
            else:
                result['link'] = None

            name_element = card.find('h3', class_='tAxDx')
            result['name'] = name_element.text if name_element else None
            
            site_element = card.find('div', class_='aULzUe')
            result['sites'] = site_element.text if site_element else None

            img_element = card.find('div', class_='ArOc1c').find('img')
            if img_element and 'src' in img_element.attrs:
                 result['img'] = img_element['src']
            else:
                result['img'] = None
            
            if result.get('price'): # Only add if there is a price
                results.append(result)

        except (AttributeError, KeyError) as e:
            print(f"Skipping a card due to a parsing error: {e}")
            continue

    if not results:
        print("No product results found.")
        return None

    return pd.DataFrame(results)

def properCompare(product):
    """
    Wrapper for the new scraping function to maintain compatibility.
    This can be removed if all calls are updated to use scrape_google_shopping.
    """
    return scrape_google_shopping(product)


