from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .datamine import scrape_product_reviews
from .compare import properCompare
from .trackProduct import trackProduct
from .compareTrack import comparetrackProduct
from pymongo import MongoClient
import pandas as df


client = MongoClient('mongodb://localhost:27017/')
db = client['UserDatabase']
email = ''

# Create your views here.
from django.contrib.auth.hashers import check_password

def home(request):
    collection = db['user']
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username, password)
        
        if not username or not password:
            return render(request, 'login.html', {'error_message': 'Please provide both username and password'})
            
        
        query = {"username": username}
        user_data = collection.find_one(query) 
        
        if user_data and check_password(password, user_data.get('password')):
            print("User with provided username and password exists.")
            request.session['username'] = user_data.get('username')
            request.session['email'] = user_data.get('email')
            return render(request,'forUsers/index.html',{'username':username})
        else:
            print("User with provided username and password does not exist.")
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    
    # If GET request, just render the login page
    return render(request, 'login.html')



        
def mine(request):
    print("-------------------------mine")
    print(request.method)
    print("-------------------------mineover")
    
    return render(request,'forUsers/mine.html')



def mindata(request):
    print(request.method)
    product_id=''
    if request.method == 'POST':
        print(request.method) 
        
        product_id_url = request.POST.get("product_id")
        if 'www.amazon.in' not in product_id_url:
            return render(request, 'forUsers/minedata.html',{'error':'not an amazon url'})
        
        product_id = product_id_url.split("/dp/")[-1].split("/")[0]
        print(product_id)
        
        df = scrape_product_reviews(product_id)
        
        if df is None:
            print("Failed to scrape reviews.")
            return redirect('mine',{'username':product_id,'error':f"Could not find reviews for {product_id}"})
        
        df = df.drop_duplicates()
                    
        return render(request, 'forUsers/minedata.html', {'data': df.to_dict('records')})
    else:
        # Handle other request methods like GET
        return render(request,'forUsers/mine.html',{'pid':product_id,'error':f"no such {product_id} found"})

    




import os
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper

def downloadfile(request, file):
    base_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = base_DIR + '/files/' + file
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 2500000
    response = StreamingHttpResponse(
        FileWrapper(
            open(thefile, 'rb'),
            chunk_size
        ),
        content_type=mimetypes.guess_type(thefile)[0]
    )
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response   



def compare(request):
    return render(request,'forUsers/compare.html')

from .compare import scrape_google_shopping

def forUsersCompare(request):
    print('----------------------------------compare')
    print(request.method)
    product=''
    data = []
    if request.method == 'GET':
        print(request.method) 
        
        product = request.GET.get("product")

        if product:
            print(product)
            df = scrape_google_shopping(product)
            if df is not None:
                data = df.to_dict('records')

    print('-------------------------------------------------')
    return render(request,'forUsers/compareProduct.html',{'data': data,'title':product})

# def createTrack(request):
#     return render(request,'forUsers/createTrack.html')


from .trackProduct import scrape_amazon_product

def track(request):
    print('--------------------------------Track')
    print(request.method)
    collection = db['trackProducts']
    email = request.session.get('email')

    if not email:
        return redirect('login')
    
    
    if request.method == 'POST':
        userData = request.POST.dict()
        product_url = request.POST.get('purl')
        if 'www.amazon.in' not in product_url:
            return render(request,'forUsers/track.html',{'error':'not an amazon product'})
        
        product_id = product_url.split("/dp/")[-1].split("/")[0]
        
        
        scraped_data = scrape_amazon_product(product_id)

        if not scraped_data:
            return render(request, 'forUsers/track.html', {'error': 'Could not retrieve product data. Please check the URL.'})

        data = {
            "emailId": email,
            "product": scraped_data.get('name'),
            "productID": product_id,
            "Price": scraped_data.get('price'),
            "imgUrl": scraped_data.get('imgUrl'),
            "link": product_url,
        }
        
        #add product to track
        result = collection.insert_one(data)
        
        #get track information for user
        query = {"emailId": email}
        userProduct = collection.find(query)
        
        return render(request,'forUsers/track.html',{'data':userProduct})
    
    if request.method == 'GET':
        #get track information for user
        query = {"emailId": email}
        userProduct = collection.find(query)
        
        return render(request,'forUsers/track.html',{'data':userProduct})
    else:
        return render(request,'forUsers/track.html')
        



from django.core.mail import send_mail
from django.conf import settings
def request(request):
    collection = db['quests']
    if request.method == 'POST':
        userData = request.POST.dict()
        
        print(userData.get('userid'))
        data = {
        "username": userData.get('userid'),
        "mailId": userData.get('useremail'),
        "type":userData.get("retype"),
        "title": userData.get('titelre'),
        "comment": userData.get('recomment')
        }
        
        query = {"username": userData.get('userid')}
        user_exists = collection.find({ "username":userData.get('userid')})
        # print(user_exists)
        message = f"Dear {userData.get('')},\n thank you for the response on,\n {userData.get('recomment')} \n we have started work on it."
        
        if user_exists is not None:
            send_mail(
                'Received ' + userData.get("retype"),
                message,
                settings.EMAIL_HOST_USER,
                [userData.get('useremail')],
            )
        
        
        
        
        
        print(data)
        result = collection.insert_one(data)
        if result.inserted_id:
            print("data inserted successfully")
            return render(request,'forUsers/request.html',{'re':'sucess'})
    else:
        return render(request,'forUsers/request.html')