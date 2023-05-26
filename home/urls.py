from .import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('home',views.index),
    path('login',views.login,name='login'),
    path('contact',views.contact),
    path('about',views.about),
    path('signup',views.signup,name='signup'),
    path('bookings',views.bookings,name='bookings'),
    path('bookings2',views.bookings2,name='bookings2'),
    path('enquiry',views.enquiry,name='enquiry'),
]