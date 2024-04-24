from django.shortcuts import render,redirect
from django.http import HttpResponse
from pymongo import MongoClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import random


#database connection
client = MongoClient('mongodb+srv://pruthu:pruthurajdata@atlascluster.ppge8u6.mongodb.net/')
db = client['UserDatabase']


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
    
    collection = db['user']
    
    # Prepare data to insert
    data = {
        "first name": userData.get('fname'),
        "last name": userData.get('lname'),
        "email": userData.get('email'),
        "number": int(userData.get('num')),
        "gender": userData.get('gender'),
        "DOB": userData.get('bdate'),
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

otp = 0000

from django.core.mail import send_mail
from django.conf import settings

changePasswordForEmail = ''

def forgotPassword(request):
    print(request.method)
    print('forgotPassword')
    collection = db['user']
    
    if request.method == 'GET':   
        userData = request.GET.dict()
        print(userData.get('email'))
        
        
        query = {"email": userData.get('email')}
        
        if userData.get('email') == None:
            return render(request,'forgotPassword.html')
            
        
        
        collection = db['user']
        
        user_exists = collection.find_one(query) is not None
        
        if user_exists is None:
            print("user doesnot exist")
            return render(request,'forgotPassword.html',{'error':"User does not exist"})
        else:
            print("user exist")

            global changePasswordForEmail
            changePasswordForEmail = userData.get('email')
            global otp 
            otp = random.randint(1000, 9999)
            message = "your otp is " + str(otp) + " and don't share it with anyone else."
            send_mail(
                'OTP ',
                message,
                settings.EMAIL_HOST_USER,
                [userData.get('email')],
            )
            return render(request,'passwordOTP.html',{'email':userData.get('email')})
    else:
        return render(request,'forgotPassword.html')


@csrf_protect
def passwordOTP(request):
    print("passwordOTP")
    collection = db['user']
    global changePasswordForEmail
    
    if request.method == 'GET':   
        userData = request.GET.dict()
        
        global otp 
        uotp = ''
        
        uotp = userData.get('ot1')
        uotp += userData.get('ot2')
        uotp += userData.get('ot3')
        uotp += userData.get('ot4')
        
        print(uotp + " " + str(otp))
        if int(uotp) == int(otp):
            print("otp verified")
            otp = ''
            return render(request,'resetPassword.html')
        else:
            return render(request,'passwordOTP.html',{'error':"OTP does not match"})
        
    if request.method == 'POST':
        print(request.method + " " + changePasswordForEmail)
        userData = request.POST.dict()
        collection.update_one({'email': changePasswordForEmail}, {'$set': {'password': userData.get('password')}})
        changePasswordForEmail = ''
        return redirect('login')
    else:
        return render(request,'passwordOTP.html')




def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')