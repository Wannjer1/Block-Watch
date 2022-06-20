

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'blockapp/index.html')


# function to add neighbourhood
def AddNeighbourhood(request, username):
    # remember to link this function to the profile model
    if request.method == 'POST':
        form = AddNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.neighbourhood_admin = request.user
            neighbourhood.save()
            messages.success(request, 'A Neighbourhood Was Created Successfully!')
            return redirect('MyNeighbourhoods', username=username)
        else:
            messages.error(request, "A Neighbourhood Wasn't Created!")
            return redirect('AddNeighbourhood')
    else:
        form = AddNeighbourhoodForm()
    return render(request, 'AddNeighbourhood.html', {'form':form})

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

# function to add business
def AddBusiness(request):
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
