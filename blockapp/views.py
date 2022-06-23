

from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.views import generic
from .forms import *
from django.contrib.auth.views import LoginView  
from django.core.exceptions import PermissionDenied  
from django.forms.models import inlineformset_factory
from django.views import View


from django.contrib import messages


# Create your views here.

# sign up view


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/register.html'


class AdminLoginView(LoginView):
    template_name ='registration/login.html'



def home(request):
    neighbourhoods = NeighbourHood.objects.all()
    return render(request, 'blockapp/index.html', {'neighbourhoods':neighbourhoods})




# function to add neighbourhood
@login_required
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
@login_required
def MyNeighbourhoods(request):
#    remember to link with the profile model
    neighbourhoods = NeighbourHood.objects.all()
    for neighbourhood in neighbourhoods:
        print(neighbourhood.title)
        print(neighbourhood.description)
    return render(request, 'blockapp/neighbourhoods.html', {'neighbourhoods':neighbourhoods})

# function to render single/individual blocks
@login_required
def SingleNeighbourhood(request, title):
    neighbourhood = get_object_or_404(NeighbourHood, title=title)
    businesses = Business.objects.filter(neighbourhood = neighbourhood.id).all()
    posts = Post.objects.filter(neighbourhood = neighbourhood.id).all()

    return render(request, 'blockapp/singleblock.html', {'neighbourhood': neighbourhood, 'businesses':businesses, 'posts':posts})

# function to view users posts 
def MyPosts(request):
    posts = Post.objects.all()
    return render(request, 'blockapp/post.html', {'posts':posts})

# funtion to create a new post
@login_required
def new_post(request):
    
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            neighbourhood = form.cleaned_data['neighbourhood']
           

            neighbourhood_obj = NeighbourHood.objects.get(pk=int(neighbourhood))
            new_post = Post(title = title, neighbourhood = neighbourhood_obj, description = description)
            new_post.save()

            messages.success(request, ' Your Post Was Created Successfully!')
            return redirect('MyPosts')

        else:
    
            messages.error(request, "Your Post Wasn't Created!")
            return redirect('AddPost')
    else:
        form = NewPostForm()
    return render(request, 'blockapp/addpost.html', {'form':form})




# function to add business
@login_required
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
            new_business = Business(name = name, email = email, neighbourhood = neighbourhood_obj, description = description)
            new_business.save()

            messages.success(request, 'A Business Was Created Successfully!')
            return redirect('MyBusinesses')

        else:
            messages.error(request, "A Business Wasn't Created!")
            return redirect('AddBusiness')

    else:
        form = BusinessForm()
    
    return render(request, 'blockapp/addbiz.html', {'form': form,})

# function to show users business post
def MyBusinesses(request):
#    remember to link this with the user profile
  
    businesses = Business.objects.all()
    return render(request, 'blockapp/business.html', {'businesses':businesses})

# function to enable users search for posted businesses
@login_required
def Search(request):
    if request.method == 'POST':
        search = request.POST['BusinessSearch']
        print(search)
        businesses = Business.objects.filter(name__icontains = search).all()
        return render(request, 'blockapp/search.html', {'search':search, 'businesses':businesses})
    else:
        return render(request, 'blockapp/search.html')


# user profile view
class ProfileView(View):
    def get(self, request):
        user = request.user
        user_profile = get_object_or_404(Profile, user=user)
        print(user_profile)
        ctx = {
            'profile': user_profile
        }
        return render(request, 'blockapp/profile.html', ctx)


# user profile page
@login_required() # only logged in users should access this
def edit_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # The sorcery begins from here, see explanation https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('title', 'bio', 'avatar','neighbourhood'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/profile/')

        return render(request, "blockapp/updateProfile.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied