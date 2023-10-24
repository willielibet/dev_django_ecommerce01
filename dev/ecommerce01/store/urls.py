from django.urls import path

#import the store/views.py file
from . import views 

#create a list of our urls patterns
urlpatterns = [
    path('', views.store, name='store'),

    #path for individual product page where we can see 
    #more info and added to the cart.
    #slug = marvin-black-shoe.
    #we need to create the views.product_info that references <slug:slug>
    #and returns the necessary data. 
    path('product/<slug:slug>', views.product_info, name='product-info')

]