from django.shortcuts import render

#import our category model and product model
from . models import Category, Product

from django.shortcuts import get_list_or_404


# Create your views here.

def store (request):
    #to return all of our product in the store.html page.
    all_products = Product.objects.all()
    #create a context dicitionary and take all products as a key-value pair.
    context = {'my_products_key': all_products}
    #pass the context dictionary.
    return render(request, 'store/store.html', context=context)
    #return render(request, 'store/store.html', context) -> this also works.
    #return render(request, 'store/store.html')

#category view.
#add this view in the ecommerce01/ecommerce01/settngs.py file in TEMPLATES.
def categories(request):
    #query the db
    all_cagetories = Category.objects.all()

    #'all_categories': all_cagetories -> dictionary
    return {'all_categories': all_cagetories}

def product_info(request, slug):
    #i want to get the product where the slug is equal to the slug (in the models).
    #we set our slug here:   slug = models.SlugField(max_length=255) in the products 
    #and categories classes.
    #if product doest not exist, throw a 404 error.
    product = get_list_or_404(Product, slug=slug)

    context = {'product': product}
    return render(request, 'store/product-info.html', context)