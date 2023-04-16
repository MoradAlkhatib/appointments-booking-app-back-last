from django.db import models
from user.models import User
# Create your models here.


# time will be stored in minutes
class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    tags = models.ManyToManyField('Tag')
    shop = models.ForeignKey("shop.Shop", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='service_pictures', null=True, blank=True)
    video = models.FileField(upload_to='service_videos', null=True, blank=True)
    is_available=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)
    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=80) #  minimum amount of time required between a booking being made and the service being offered
    booking_lead_time = models.IntegerField(default=0)
    booking_cutoff_time=models.IntegerField(default=0) #  a TimeField to specify the latest time at which a booking can be made for the service on a given day
    is_cancelable=models.BooleanField(default=True)
    cancel_cutoff_time=models.IntegerField(default=0)
    def __str__(self):
        return self.name

    @property
    def rate(self):
        '''
        rate method that get all rate that related to this shop
        that got from the users and calculate average for them.
        '''
        return ServiceReview.objects.filter(service=self).aggregate(avg_rating=models.Avg('rating'))['avg_rating']


class ServiceReview(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name