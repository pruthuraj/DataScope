import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}

def trackProduct(productid):
    product_url = f'https://www.amazon.in/dp/{productid}'
    
    
    
    response = requests.get(product_url, headers=headers)
        
    
    soup = bs(response.content, 'html.parser')
        
    # Extract product name
    name = soup.find('span', id='productTitle').get_text(strip=True)
        
    # Extract product image URL
    img = soup.find('div', id='imgTagWrapperId').find('img')
    srcimage = img['src']
        
    # Extract product price
    price = soup.find('span', class_='a-price-whole').get_text(strip=True)
    
    data = {
        'name': name,
        'price': price,
        'imgUrl': srcimage
    }
        
    return data


