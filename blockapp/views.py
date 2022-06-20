

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'blockapp/index.html')


# function to add neighbourhood
def AddNeighbourhood(request):
    # remember to link this function to the profile model
    if request.method == 'POST':
        form = AddNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.neighbourhood_admin = request.user
            neighbourhood.save()
            messages.success(request, 'A Neighbourhood Was Created Successfully!')
            return redirect('MyNeighbourhoods')
        else:
            messages.error(request, "A Neighbourhood Wasn't Created!")
            return redirect('AddNeighbourhood')
    else:
        form = AddNeighbourhoodForm()
    return render(request, 'blockapp/addhood.html', {'form':form})

# function to show users neighbourhood
def MyNeighbourhoods(request):
#    remember to link with the profile model
    neighbourhoods = NeighbourHood.objects.all()
    for neighbourhood in neighbourhoods:
        print(neighbourhood.title)
        print(neighbourhood.description)
    return render(request, 'blockapp/neighbourhoods.html', {'neighbourhoods':neighbourhoods})

# funtion to create a new post
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'blockapp/addpost.html', {'form': form,'current_user': current_user}) 

# function to view users posts 
def MyPosts(request):
    posts = Post.objects.filter.all()
    return render(request, 'blockapp/posts.html', {'posts':posts})


# function to add business
def AddBusiness(request):
    # remember to add profile model
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            neighbourhood = form.cleaned_data['neighbourhood']
            description = form.cleaned_data['description']

            neighbourhood_obj = NeighbourHood.objects.get(pk=int(neighbourhood))

        else:
            messages.error(request, "A Business Wasn't Created!")
            return redirect('home')

    else:
        form = BusinessForm()
    
    return render(request, 'blockapp/addbiz.html', {'form': form,})

# function to show users business post
def MyBusinesses(request):
#    remember to link this with the user profile
  
    businesses = Business.objects.filter.all()
    return render(request, 'blockapp/business.html', {'businesses':businesses})

# function to enable users search for posted businesses
def Search(request):
    if request.method == 'POST':
        search = request.POST['BusinessSearch']
        print(search)
        businesses = Business.objects.filter(name__icontains = search).all()
        return render(request, 'blockapp/search.html', {'search':search, 'businesses':businesses})
    else:
        return render(request, 'blockapp/search.html')





