from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from .models import *
class ProductForm(ModelForm):
    '''name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'name',
                                                         'name':'name',
                                                         'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
    anons = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name',
                                                                          'name':'name',
                                                                          'class':'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
                                                         'id':'file_input',
                                                   'type':'file'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                                         'id': 'name',
                                                         'name':'name',
                                                         'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))'''
    #cat = forms.ChoiceField(widget=forms.ChoiceField(attrs={'id':'category'}))
    class Meta:
        model = Product
        fields = ('name', 'anons', 'status', 'image', 'price', 'cat', )

class ProductChangeForm(ModelForm):
    name = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'type': 'text',
                                                                        'id': 'name',
                                                                        'name': 'name',
                                                                        'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))
    anons = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'id': 'name',
                                                                          'name': 'name',
                                                                          'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400',
        'id': 'file_input',
        'type': 'file'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
                                                             'id': 'name',
                                                             'name': 'name',
                                                             'class': 'w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'}))

    # cat = forms.ChoiceField(widget=forms.ChoiceField(attrs={'id':'category'}))
    class Meta:
        model = Product
        fields = ('name', 'anons', 'status', 'image', 'price', 'cat',)
