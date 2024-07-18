from django.shortcuts import render
from .models import InformationSystem
def index(request):

    IS=InformationSystem.objects.order_by('-published')

    return render(request,"welcome/index.html",{"IS":IS})
