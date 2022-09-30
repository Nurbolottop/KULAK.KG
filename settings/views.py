import imp
from django.shortcuts import render
from settings.models import Setting
# Create your views here.
def index(request):
    return render(request,'index.html')