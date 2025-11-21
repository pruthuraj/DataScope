import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}

from django.core.mail import send_mail
from django.conf import settings

def comparetrackProduct(productid, emailid):
    headers = {
        'User-Agent': 'Your User Agent String',  # Replace with your user agent
    }
    
    for item in productid:
        if isinstance(item, dict):
            product_id = item.get('productID')
            ip = item.get('Price')
            
            if product_id:
                product_url = f'https://www.amazon.in/dp/{product_id}'
                
                response = requests.get(product_url, headers=headers)
                soup = bs(response.content.decode('utf-8'), 'html.parser')
                price_elem = soup.find('span', class_='a-price-whole')
                
                if price_elem:
                    # Extract text from price_elem and clean it (remove commas and dots)
                    price = price_elem.get_text(strip=True)
                    
                    if price < ip:
                        message = (
                            f"Dear customer,\n"
                            f"The price of the product you are tracking has decreased from {ip} to {price}.\n"
                            f"Product Link: {product_url}"
                        )
                        
                        send_mail(
                            f'Tracked Product Price Decrease: {product_id}',
                            message,
                            settings.EMAIL_HOST_USER,
                            [emailid],
                        )



# def comparetrackProduct(productid,emailid):
#     for item in productid:
#         if isinstance(item, dict):
#             product_id = item.get('productID')
#             ip = item.get('Price')
            
            
#             product_url = f'https://www.amazon.in/dp/{product_id}'
#             response = requests.get(product_url, headers=headers)
#             soup = bs(response.content, 'html.parser')            
#             price_elem = soup.find('span', class_='a-price-whole').replace(',','').replace(".","")
#             price = 0
                 
#             if price_elem:
#                 price = int(price_elem.get_text(strip=True))
            
#             if price < int(ip):
#                 message = (
#                     f"Dear customer,\n"
#                     f"The price of the product you are tracking has decreased from {ip} to {price}.\n"
#                     f"Product Link: {product_url}"
#                 )
                        
#                 send_mail(
#                     f'Tracked Product Price Decrease: {item}',
#                     message,
#                     settings.EMAIL_HOST_USER,
#                     [emailid],
#                 )