from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .datamine import mineUserProduct 
from .compare import properCompare
from .trackProduct import trackProduct
from pymongo import MongoClient
import pandas as df


client = MongoClient('mongodb+srv://pruthu:pruthurajdata@atlascluster.ppge8u6.mongodb.net/')
db = client['UserDatabase']
email = ''

# Create your views here.
def home(request):
    collection = db['user']
    
    if request.method == 'GET':
        
        username = request.GET.get('username')
        password = request.GET.get('password')
        
        print(username, password)
        
        if username is None and password is None:
            return render(request, 'login.html', {'error_message': 'please login first'})
            
        
        query = {"username": username}
        user_exists = collection.find_one(query) 
        user_existsBool = collection.find_one(query) is not None
        
        global email
        email = user_exists.get('email')
        
        
        #check if user exist
        if user_existsBool:
            
            query = {"username": username, "password": password}
            user_exists = collection.find_one(query) is not None
            
            # check if password is correct
            if user_exists:
                print("User with provided username and password exists.")
                return render(request,'forUsers/index.html',{'username':username})
            else:
                print("User with provided username and password does not exist.")
                return render(request, 'login.html', {'error_message': 'Invalid password'})
        else:
            # User doesn't exist or provided incorrect credentials
            return render(request, 'login.html', {'error_message': 'user does not exist'})
    return HttpResponse('user not found')



        
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
        
        product_id = request.POST.get("product_id")
        if 'www.amazon.in' not in product_id:
            return render(request, 'forUsers/minedata.html',{'error':'not an amazon url'})
        product_id = product_id.split("/dp/")[-1].split("/")[0]
        print(product_id)
        df = mineUserProduct(product_id).drop_duplicates()
        
        #if no such id found
        if type(df) == str:
            print(df)
            return redirect('mine',{'username':product_id,'error':f"no such {product_id} found"})
        else:            
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

def forUsersCompare(request):
    print('----------------------------------compare')
    print(request.method)
    product=''
    if request.method == 'GET':
        print(request.method) 
        
        product = request.GET.get("product")

        print(product)
        df = properCompare(product)
    print('-------------------------------------------------')
    return render(request,'forUsers/compareProduct.html',{'data': df.to_dict('records'),'title':product})

# def createTrack(request):
#     return render(request,'forUsers/createTrack.html')

def track(request):
    print('--------------------------------Track')
    print(request.method)
    collection = db['trackProducts']
    global email
    
    
    if request.method == 'POST':
        userData = request.POST.dict()
        product = request.POST.get('purl')
        if 'www.amazon.in' not in userData.get('purl'):
            return render(request,'forUsers/track.html',{'error':'not an amazon product'})
        product_id = product.split("/dp/")[-1].split("/")[0]
        
        
        p = trackProduct(product_id)
        data = {
            "emailId": email,
            "product": p.get('name'),
            "productID":product_id,
            "Price": p.get('price'),
            "imgUrl": p.get('imgUrl'),
            "link": userData.get('purl'),
        }
        
        #add product to track
        result = collection.insert_one(data)
        
        #get track information for user
        query = {"emailId": email}
        userProduct = collection.find(query)
        print(userProduct)
        return render(request,'forUsers/track.html',{'data':userProduct})
    if request.method == 'GET':
        
        #get track information for user
        print(email)
        query = {"emailId": email}
        userProduct = collection.find(query)
        print(userProduct)
        
        
        
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
        user_exists = collection.find({ "user": "pruthu" }, { "name": 1, "_id": 0 })
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