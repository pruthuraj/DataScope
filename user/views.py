from django.shortcuts import render
from django.http import HttpResponse 
from .datamine import mineUserProduct 

# Create your views here.
def home(request):
    if (request.method == 'GET'):
        username = request.GET.get("username")
        password = request.GET.get("password")
        print( username, password)
        return render(request,'forUsers/index.html',{'username':username})
    return HttpResponse('user not found')






        
def mine(request):
    return render(request,'forUsers/mine.html')


def mindata(request):
    if (request.method == 'POST'):
        mine = request.POST.dict()
        product_id = mine.get("user_type")
        print(product_id)
        mineUserProduct(product_id)
    # mineUserProduct('B08HQW9SGP')
    return