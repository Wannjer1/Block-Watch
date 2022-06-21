from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


CATEGORIES = [
    ('1', 'Crimes and Safety'),
    ('2', 'Health Emergency'),
    ('3', 'Recommendations'),
    ('4', 'Fire Breakouts'),
    ('5', 'Lost and Found'),
    ('6', 'Death'),
    ('7', 'Event'),
]

# neighbourhood form
class AddNeighbourhoodForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Title','class': 'form-control mb-4'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Description','class': 'form-control mb-4','rows': 3,}))
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Location','class': 'form-control mb-4'}))
    neighbourhood_logo = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'dropify', 'data-height':300, 'data-max-file-size':"1M"}))
    health_department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Health Department','class': 'form-control mb-4'}))
    police_department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Police Department','class': 'form-control mb-4'}))

    class Meta:
        model = NeighbourHood
        fields = ('title','description','location','neighbourhood_logo','health_department','police_department')


# new post form 
class NewPostForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Post Title'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'rows': 5, 'placeholder':'Description'}))
    category = forms.ChoiceField(choices=CATEGORIES, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'placeholder':'Select Category'}))
    neighbourhood = forms.ChoiceField(label=u'Select Your Neighbourhood', required=True, widget=forms.Select(attrs={'class': 'form-control mb-4'}))
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'dropify', 'data-height':300, 'data-max-file-size':"1M"}))

    def __init__(self, *args, **kwargs):
        super(NewPostForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.title) for e in NeighbourHood.objects.all()]


# business form
class BusinessForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Business Name','class': 'form-control mb-4'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Business Description','class': 'form-control mb-4','rows': 5,}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Business Email','class': 'form-control mb-4'}))
    neighbourhood = forms.ChoiceField(required=True, widget=forms.Select(attrs={'placeholder': 'Neighbourhood','class': 'form-control mb-4'}))

    def __init__(self, *args, **kwargs):
        super(BusinessForm, self).__init__(*args, **kwargs)
        self.fields['neighbourhood'].choices = [(e.id, e.title) for e in NeighbourHood.objects.all()]
