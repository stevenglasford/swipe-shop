from django.shortcuts import render
from django.http import HttpResponse


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