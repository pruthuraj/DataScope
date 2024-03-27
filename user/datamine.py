import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os

#--------------------------------
#----              variables
#----------------------------------------------

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}


#--------------------------------
#----              functions to get min length of list
#----------------------------------------------

def min_length_of_lists(list1, list2, list3, list4):
    min_length = min(len(list1), len(list2), len(list3), len(list4))
    return min_length


#--------------------------------
#----              functions to get page and data  as well
#----------------------------------------------------------------

def mineUserProduct(product_id):
    pageLimit = 15
     
    product_url = f'https://www.amazon.in/dp/{product_id}'
    url = f'https://www.amazon.in/product-reviews/{product_id}/pageNumber='
    page_num = 1
    df = pd.DataFrame()
    
    # if product_id is '' or len(product_id) != 10:
    #     return print("product_id cannot be null or does not exist")
      
    while True:
        
        #--------------------------------
        #----      code to send request page 
        #----------------------------------------------------------------
        
        page = None
        while page is None or page.status_code != 200:
            page = requests.get(url + str(page_num), headers=headers)

            if page.status_code == 404:
                return "Page not found."
                
            
        #--------------------------------
        #----      code to get page data i.e html element
        #----------------------------------------------------------------    
        
        
        print(url + str(page_num))
        soup = bs(page.content, 'html.parser')

        names_list = [name.get_text() for name in soup.find_all('span', class_='a-profile-name')[2:]]
        
        #          if names_list is false then it means that is it the 
        #          page is not found In Python,( an empty list evaluates to False )
        if not names_list:
            break

        review_titles_list = [title.get_text()[19:-1] for title in soup.find_all('a', class_='review-title')]
        date_reviews_list = [date.get_text() for date in soup.find_all('span', class_='review-date')]
        star_ratings_list = [star.get_text().replace(' out of 5 stars', '') for star in soup.find_all('span', class_='a-icon-alt')]

        #--------------------------------
        #----      code to check min length of list 
        #----------------------------------------------------------------

        min_len = min_length_of_lists(
            names_list,
            review_titles_list,
            date_reviews_list,
            star_ratings_list
            )

        #--------------------------------
        #----      store the list in a data frame according to smallest list
        #----      to justify why, all the list that are to be stored in data frame
        #----      should be of same length, but here sime data might be missing so
        #----      it it stored according to minimum length of list. 
        #----------------------------------------------------------------

        temp_df = pd.DataFrame({
            'Customer Names': names_list[:min_len],
            'Review Title': review_titles_list[:min_len],
            'Review Date': date_reviews_list[:min_len],
            'Rating': star_ratings_list[:min_len]
        })

        df = pd.concat([df, temp_df], ignore_index=True)
        page_num += 1
        if page_num > pageLimit:
            break
        
    directory = 'files'  # Change this to your desired directory path

# Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Save DataFrame to a CSV file inside the directory
    df.to_csv(os.path.join(directory, 'data.csv'), index=False)
    df.to_excel(os.path.join(directory, 'data.csv'), index=False)
    print("successfull mining ")
    return 

