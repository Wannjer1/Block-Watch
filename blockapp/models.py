from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICES = [ 
    ('1', 'Crimes and Safety'),
    ('2', 'Health Emergency'),
    ('3', 'Recommendations'),
    ('4', 'Fire Breakouts'),
    ('5', 'Lost and Found'),
    ('6', 'Death'),
    ('7', 'Event'),
]
# post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'post_img/')
    description = models.TextField(blank=True, max_length=255)
    category = models.CharField(max_length=255,choices=CHOICES)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    # rememeber to add profile foreign key

    def __str__(self):
        return str(self.title)

    def save_post(self):
        self.save()


# business model
class Business(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)
    # REMEMBER TO ADD PROFILE FIELD

    def __str__(self):
        return str(self.name)

    def get_businesses(self):
        '''Method to get all businesses '''
        businesses = Business.objects.all()
        return businesses

    def save_business(self):
        '''Method to save businesses'''
        self.save()

    def delete_business(self):
        '''Method to delete businesses'''
        self.delete()

    def update_business(self):
        '''Method to update businesses'''
        self.update()

    def find_business(self, business_id):
        business = Business.objects.filter(self=business)
        return business

# neighbourhood model
class NeighbourHood(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(max_length=255,null=True, blank=True)
    location = models.CharField(max_length=150, verbose_name='Neighbourhood Location', null=True, blank=True)
    neighbourhood_logo =  models.ImageField(upload_to = 'post_img/')
    neighbourhood_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    health_department = models.CharField(max_length=15, null=True, blank=True)
    police_department = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    