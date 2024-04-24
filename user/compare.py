import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


header = (
    {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    ,'Accept-Language':'en-IN , en;q=0.5'}
)

def min_length_of_lists(list1, list2, list3, list4):
    min_length = min(len(list1), len(list2), len(list3), len(list4))
    return min_length

def remove_content_between_brackets(input_string):
    return re.sub(r'<[^>]*>', '', input_string)

def getProduct(product):
    product = product.replace(' ','+')
    url = 'https://www.google.com/search?sca_esv=88f53b0a7b860e25&hl=en&tbm=shop&sxsrf=1&q='
    url =url + product
    
    page = None
    while page is None or page.status_code != 200:
        page = requests.get(url , headers=header)
        if page.status_code == 404:
            print("Page not found.")
            return "Page not found."
    soup = bs(page.content,'html.parser')
    
        
    links = soup.find_all('a', class_='shntl')
    price = soup.find_all('span',class_ = 'QIrs8')
    names = soup.find_all('h3', class_='tAxDx')
    sites = soup.find_all('div',class_ = 'aULzUe')
    
    href_values = [link['href'] for link in links]
    cleaned_href_values = [href_value.replace('/url?url=', '') for href_value in href_values]
    cleaned_href_values = list(set(cleaned_href_values))
    
    cleaned_price = [remove_content_between_brackets(name.get_text()) for name in price]
    filtered_data = [row for row in cleaned_price if '$' or '₹' in row]
            
    cleaned_names = [remove_content_between_brackets(name.get_text()) for name in names]

    # sites.remove(sites[0])
    cleaned_sites = [remove_content_between_brackets(name.get_text()) for name in sites]

    
    minlen = min_length_of_lists(cleaned_sites,cleaned_names,filtered_data,cleaned_href_values)

    df = pd.DataFrame({
        'name': cleaned_names[:minlen],
        'sites': cleaned_sites[:minlen],
        'price': filtered_data[:minlen],
        'link': cleaned_href_values[:minlen]
    })
    df = df.drop_duplicates(ignore_index = True )

    
    return df

def properCompare(product):
    product = product.replace(' ','+')
    url = 'https://www.google.com/search?sca_esv=88f53b0a7b860e25&hl=en&tbm=shop&sxsrf=1&q='
    url =url + product
    
    page = None
    while page is None or page.status_code != 200:
        page = requests.get(url , headers=header)
        if page.status_code == 404:
            print("Page not found.")
            return "Page not found."
    soup = bs(page.content,'html.parser')
    
    site = []
    price = []
    name = []
    image = []
    link = []
    
    for card in soup.find_all('div', class_='sh-dgr__content'):
        if card.find('span',class_='OFFNJ') is None:
            continue
        
        price.append(card.find('span',class_='OFFNJ').text)  
        link.append(card.find('a',class_='xCpuod')['href'])
        
        if card.find('h3',class_='tAxDx') is not None:
            name.append(card.find('h3',class_='tAxDx').text)
        else:
            name.append("")
        if card.find('div',class_='aULzUe') is not None:
            site.append(card.find('div',class_='aULzUe').text)
        else:
            name.append("")
        image.append(card.find('div',class_='ArOc1c').find('img')['src'])

    links = [href_value.replace('/url?url=', '') for href_value in link]
    
    df = pd.DataFrame({
        'name': name,
        'sites': site,
        'price': price,
        'link': links,
        'img': image
    })
    return df

