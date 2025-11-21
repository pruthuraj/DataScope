import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}

def scrape_product_reviews(product_id: str, page_limit: int = 25) -> pd.DataFrame | None:
    """
    Scrapes the reviews for a given Amazon product ID.

    Args:
        product_id: The Amazon Standard Identification Number (ASIN) of the product.
        page_limit: The maximum number of review pages to scrape.

    Returns:
        A pandas DataFrame containing the review data, or None if scraping fails.
    """
    if not product_id or len(product_id) != 10:
        print("Invalid product_id provided.")
        return None

    base_url = f'https://www.amazon.in/product-reviews/{product_id}/pageNumber='
    reviews_data = []

    for page_num in range(1, page_limit + 1):
        url = base_url + str(page_num)
        print(f"Scraping page: {url}")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            time.sleep(1) # Be a good citizen and don't spam requests
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch page {page_num}. Error: {e}")
            continue # Try the next page

        soup = bs(response.text, 'html.parser')
        
        # Find all review containers
        review_containers = soup.find_all('div', {'data-hook': 'review'})

        if not review_containers:
            print("No more reviews found. Stopping.")
            break

        for review in review_containers:
            name = review.find('span', class_='a-profile-name')
            review_title = review.find('a', {'data-hook': 'review-title'})
            date = review.find('span', {'data-hook': 'review-date'})
            star_rating = review.find('i', {'data-hook': 'review-star-rating'})

            reviews_data.append({
                'Names': name.get_text(strip=True) if name else None,
                'Review': review_title.get_text(strip=True) if review_title else None,
                'Date': date.get_text(strip=True) if date else None,
                'Rating': float(star_rating.get_text(strip=True).split(' ')[0]) if star_rating else None
            })

    if not reviews_data:
        print("No reviews were scraped.")
        return None

    df = pd.DataFrame(reviews_data)
    
    # Save to files
    directory = 'files'
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    csv_path = os.path.join(directory, 'data.csv')
    excel_path = os.path.join(directory, 'data.xlsx')

    df.to_csv(csv_path, index=False)
    df.to_excel(excel_path, index=False)
    
    print(f"Successfully mined {len(df)} reviews.")
    return df

def mineUserProduct(product_id):
    """
    Wrapper for the new scraping function to maintain compatibility.
    This can be removed if all calls are updated to use scrape_product_reviews.
    """
    return scrape_product_reviews(product_id)