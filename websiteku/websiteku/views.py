from sys import implementation
from urllib import request


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')