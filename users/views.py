'''Users views'''

# Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    '''Login view'''
    return render(request, 'users/login.html')
