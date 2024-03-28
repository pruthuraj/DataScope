from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .datamine import mineUserProduct 
from pymongo import MongoClient
import pandas as df


client = MongoClient('mongodb+srv://pruthu:pruthurajdata@atlascluster.ppge8u6.mongodb.net/')
db = client['UserDatabase']
collection = db['user']

# Create your views here.
def home(request):
    if request.method == 'GET':
        
        username = request.GET.get('username')
        password = request.GET.get('password')

        
        
        query = {"username": username}
        user_exists = collection.find_one(query) is not None
        
        #check if user exist
        if user_exists:
            
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
    user = request.GET.get('username')
    print(user)
    print("-------------------------mineover")
    if user is None:
        return redirect('/login', {'error_message': 'login is for it'})
    return render(request,'forUsers/mine.html',{'username':user})



def mindata(request):
    print(request.method)
    user =  ''
    if request.method == 'POST':
        print(request.method)  # This prints the request method (e.g., 'POST')
        user = request.POST.get('username')
        product_id = request.POST.get("product_id")  # Use request.POST.get to safely retrieve values

        print(product_id)
        df = mineUserProduct(product_id).drop_duplicates()
        
        #if no such id found
        if type(df) == str:
            print(df)
            return redirect('mine',{'username':user,'pid':product_id,'error':f"no such {product_id} found"})
        else:            
            return render(request, 'forUsers/minedata.html', {'data': df.to_dict('records'),'username':user})
    else:
        # Handle other request methods like GET
        return redirect('mine',{'username':user,'pid':product_id,'error':f"no such {product_id} found"})

    




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

def track(request):
    return render(request,'forUsers/track.html')

def createTrack(request):
    return render(request,'forUsers/createTrack.html')

def request(request):
    return render(request,'forUsers/request.html')

