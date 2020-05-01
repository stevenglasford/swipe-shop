from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD


# Create your views here.
def index(request):
    return render(request, 'main_page/index.html')


def list(request):
    return render(request, 'listings/index.html')


def messages(request):
    return render(request, 'messages/index.html')


def new_list(request):
    return render(request, 'new_listings/index.html')


def profile(request):
    return render(request, 'profile/index.html')
=======

# Create your views here.

def main(request):
    return render(request, 'main_app/main_page/index.html')
    
def profile(request):
    return render(request, 'main_app/profile/profile.html')
>>>>>>> 8d600482e5b8aef9dfeefe1082d856576bc440e1
