# from django import forms
# from .models import Movie
#
#
# class MovieForm(forms.ModelForm):
#     class Meta:
#         Model = Movie
#         fields = ['name', 'desc', 'year', 'img']
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'desc','year','img']