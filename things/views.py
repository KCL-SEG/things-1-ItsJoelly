from django.shortcuts import render

def thingsView(request):
    return render(request, 'thingweb.html')
