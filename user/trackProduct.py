import requests
from bs4 import BeautifulSoup as bs
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}

def scrape_amazon_product(product_id: str) -> dict | None:
    """
    Scrapes an Amazon India product page for its name, price, and image URL.

    Args:
        product_id: The Amazon Standard Identification Number (ASIN) of the product.

    Returns:
        A dictionary containing the product's name, price (as a float), and image URL,
        or None if the product page cannot be scraped successfully.
    """
    product_url = f'https://www.amazon.in/dp/{product_id}'
    
    try:
        response = requests.get(product_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product page: {e}")
        return None

    soup = bs(response.text, 'html.parser')
    
    data = {'name': None, 'price': None, 'imgUrl': None}

    # Extract product name
    try:
        name_element = soup.find('span', id='productTitle')
        if name_element:
            data['name'] = name_element.get_text(strip=True)
    except AttributeError:
        print("Could not find product name.")

    # Extract product image URL
    try:
        img_container = soup.find('div', id='imgTagWrapperId')
        if img_container:
            img_element = img_container.find('img')
            if img_element and 'src' in img_element.attrs:
                data['imgUrl'] = img_element['src']
    except AttributeError:
        print("Could not find product image.")

    # Extract product price
    try:
        # Try to find the price in the most common element
        price_element = soup.find('span', class_='a-price-whole')
        if price_element:
            price_text = price_element.get_text(strip=True)
            # Remove commas and currency symbols, then convert to float
            cleaned_price = re.sub(r'[^\d.]', '', price_text)
            if cleaned_price:
                data['price'] = float(cleaned_price) # type: ignore
    except (AttributeError, ValueError):
        print("Could not parse product price.")

    # Return data only if we have at least a name
    if data['name']:
        return data
    else:
        print("Failed to scrape essential product data.")
        return None



