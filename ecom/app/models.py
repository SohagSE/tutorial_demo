from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES=(
    ('LP','Laptop'),
    ('MB','Mobile'),
    ('RM','RAM'),
    ('SP','Speaker'),
    ('CM','Camera'),
    ('PS','Processor'), 
)

STATE_CHOICES=(
    ('Asam','Asam'),
    ('Delhi','Delhi'),
    ('Gujrat','Gujrat'),
    ('Kalkata','Kalkata'),
    ('Haydrabad','haydrabad'),
)

class product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title
    
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    
    def __str__(self):
        return self.name 