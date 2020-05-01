from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'main_app/main_page/index.html')
    
def profile(request):
    return render(request, 'main_app/profile/profile.html')
