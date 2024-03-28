from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'SignUp.html')

def login(request):
    return render(request,'login.html')

@csrf_protect
def createUser(request):
    print(request.method)
    userData = request.POST.dict()
    client = MongoClient('mongodb+srv://pruthu:pruthurajdata@atlascluster.ppge8u6.mongodb.net/')
    db = client['UserDatabase']
    collection = db['user']
    
    # Prepare data to insert
    data = {
        "first name": userData.get('fname'),
        "last name": userData.get('lname'),
        "email": userData.get('email'),
        "number": userData.get('num'),
        "DOB": userData.get('gender'),
        "username": userData.get('usid'),
        "password": userData.get('pass')
    }
    
    print(data)
    
    query = {"username": userData.get('usid')}
    user_exists = collection.find_one(query) is not None
    
    if user_exists:
        return HttpResponse("user already exit")
    
    # Insert data into collection
    result = collection.insert_one(data)
    # Check if insertion was successful
    if result.inserted_id:
        print("data inserted successfully")
        return render(request,'login.html',{
            'username':userData.get('usid'),
            'password':userData.get('pass')
            })
    else:
        return HttpResponse("Failed to insert data.")



def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# def createUser(request):
    