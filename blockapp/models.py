from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'post_img/')
    description = models.TextField(blank=True, max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_post(self):
        self.save()

# business model
class Business(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def find_business(self, business_id):
        business = Business.objects.filter(self=business)
        return business

    