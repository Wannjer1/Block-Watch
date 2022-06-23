
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

CHOICES = [ 
    ('1', 'Crimes'),
    ('2', 'Health'),
    ('3', 'Nyumba Kumi meetups'),
    ('4', 'Fire Breakouts'),
    ('5', 'Lost and Found'),
    ('6', 'Death'),
    ('7', 'Event'),
]


# neighbourhood model
class NeighbourHood(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(max_length=255,null=True, blank=True)
    location = models.CharField(max_length=150,  null=True, blank=True)
    neighbourhood_logo =  models.ImageField(upload_to = 'post_img/')
    neighbourhood_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    health_department = models.CharField(max_length=15, null=True, blank=True)
    police_department = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    occupants = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    def get_neighbourhood(self):
        neighbourhoods = NeighbourHood.objects.all()
        return neighbourhoods

    def create_neighbourhod(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighborhood(self, id, title, location, county, neighbourhood_logo):
        update = NeighbourHood.objects.filter(id = id).update(title = title , location = location, neighbourhood_logo = neighbourhood_logo)
        return update

    
# profile model
class Profile(models.Model):
    avatar = models.ImageField(upload_to = 'avatar/',max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True)
    bio = models.TextField(blank=True,default='')
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)
    

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

# post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'post_img/')
    description = models.TextField(blank=True, max_length=255)
    category = models.CharField(max_length=255,choices=CHOICES)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True, null=True)
   
   

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
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True, null=True)
  
    

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

    def update_business(self, id, name, description, email, neighbourhood):
        update = NeighbourHood.objects.filter(id = id).update(name = name , description = description, email = email, neighbourhood = neighbourhood)
        return update

    def find_business(self, business_id):
        business = Business.objects.filter(self=business_id)
        return business

# join neighbourhood 
class Join(models.Model):
	'''
	Model that keeps track of what user has joined what neighbourhood
	'''
	user_id = models.OneToOneField(User,on_delete=models.CASCADE)
	hood_id = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)

	def __str__(self):
		return self.user_id

    