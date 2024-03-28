from django.contrib import admin
from django.urls import path,include
from pages import views
from user import views as userV

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('login/',views.login,name='login'),
    path('signup/',views.signup),
    path('createuser',views.createUser,name='createuser'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('home/',userV.home,name='home'),
    path('home/mine/',userV.mine,name='mine'),
    path('home/minedata/',userV.mindata,name='btnmine'),
    path('home/track/',userV.track,name='track'),
    path('home/Track/create/',userV.createTrack,name='createTrack'),
    path('home/compare/',userV.compare,name='compare'),
    path('home/compareProduct',userV.forUsersCompare,name='comparep'),
    path('home/requests/',userV.request,name='request'),
    path('download/<str:file>/', userV.downloadfile, name='downloadbtn'),
]
