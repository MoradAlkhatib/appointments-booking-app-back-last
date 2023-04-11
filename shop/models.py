from django.db import models
from  user.models import User


def default_availability_days():
    WEEKDAYS = {
        "MON": True,
        "TUE": True,
        "WED": True,
        "THU": True,
        "FRI": True,
        "SAT": True,
        "SUN":True
    }
    return WEEKDAYS

class Shop(models.Model):
   
    
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pictures = models.ManyToManyField('Picture')
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    open_time = models.TimeField()
    close_time = models.TimeField()
    description = models.TextField()
    categories = models.ManyToManyField('Category')
    social_media_link = models.URLField(max_length=200)
    # payment method will be token to be score.
    payment_method = models.CharField(max_length=200)
    availability = models.BooleanField(default=True)
    discounts = models.ManyToManyField('Discount')
    availability_days = models.JSONField(default=default_availability_days())

    

    @property
    def rate(self):
        '''
        rate method that get all rate that related to this shop
        that got from the users and calculate average for them.
        '''
        return Review.objects.filter(shop=self).aggregate(avg_rating=models.Avg('rating'))['avg_rating']

        
class Picture(models.Model):
    image = models.ImageField(upload_to='shop_pictures')
    
class Category(models.Model):
    name = models.CharField(max_length=50)

class Discount(models.Model):
    DISCOUNT_CHOICES= [('F','fixed'),('P','percentage')]
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=3, decimal_places=2)
    discount_type = models.CharField(choices=DISCOUNT_CHOICES, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    active = models.BooleanField(default=False)
    


class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)