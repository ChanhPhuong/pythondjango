from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def allcategory (request):
    return render(request, 'page/home.html')