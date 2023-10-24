from django.db import models

# Create your models here.

class Category(models.Model):

    # db_index=True -> used for query acceleration, improves memory usage, 
    # and for faster lookups in our DB table. instead of reading whole table,
    # it stops once it finds the attribute instead of reading the entire model.  
    name = models.CharField(max_length=250, db_index=True)

    # to get a particular category
    # unique=True not to have repeated categories; 1 for bags; 1 for books; 
    # 1 for shirts; 1 for pants; like 127.0.0.1:8000/shoes/nike-air-jordan -> so,
    # it is going to have the category and the product.
    slug = models.SlugField(max_length=250, unique=True)

    # define some metadata
    class Meta:
        verbose_name_plural = 'categories'

    #define a string function
    def __str__(self):
        return self.name
    
#create our product model.
#blank=True -> means this field is optional.
# images/ is a directory.
class Product(models.Model):
    #FK
    #this FK ensures that if you delete a category, then its product is also deleted.
    #null=True ensures that we do not have any null objects.
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    # define some metadata
    class Meta:
        verbose_name_plural = 'products'

    #define a string function
    def __str__(self):
        return self.title





        