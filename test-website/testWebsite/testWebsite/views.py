from django.shortcuts import render

def testPage(request):
    return render(request, 'dynamic_weather.html')