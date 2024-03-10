from django.contrib import admin
from django.urls import path,include
from pages import views

urlpatterns = [
    path('',views.index,name='home'),
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('signup/',views.signup),
    path('about/',views.about),
    path('contact/',views.contact),
]
