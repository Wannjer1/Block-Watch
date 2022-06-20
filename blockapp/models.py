from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'post_img/')
    description = models.TextField(blank=True, max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_post(self):
        self.save()

    