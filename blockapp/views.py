from multiprocessing.dummy import current_process
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import NewPostForm

# Create your views here.
def home(request):
    return HttpResponse("Trial url page for pair grouping. I am suppsed to work on the models.user stories 3,4,5")


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
    return render(request, 'blockapp/posts.html', {'form': form,'current_user': current_user}) 