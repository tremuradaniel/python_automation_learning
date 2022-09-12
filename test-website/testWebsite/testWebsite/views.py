from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def testPage(request):
    return render(request, 'dynamic_weather.html')

def homePage(request):
    return render(request, 'home.html')
