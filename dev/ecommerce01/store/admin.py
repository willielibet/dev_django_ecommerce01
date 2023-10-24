from django.contrib import admin

# Register your models here.
from . models import Category, Product

#to make use of prepopulated field.
#we are going to create two fields to specify what fields are going to be
#populated based on another field. so, in this case, the slug field will
#automatically be populated once I type the name of the category.
#our slug will be prepopulated based on the name and title of the category and product.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}





