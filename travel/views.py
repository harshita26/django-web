from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
   # dest1=Destination()
   # dest1.name='MUMBAI'
   # dest1.img='t1.jpg'
   # dest1.desc='This is bollywood city'
   # dest1.price=700
   # offer=False

   # dest2=Destination()
   # dest2.name='HYDERABED'
   # dest2.img='t2.jpg'
   # dest2.desc='This is CYBER city'
   # dest2.price=600
   # offer=True

   # dest3=Destination()
   # dest3.name='DELHI'
   # dest3.img='t3.jpg'
   # dest3.desc='This is CAPITAL OF INDIA'
   # dest3.price=800
   # offer=True

   # dests=[dest1, dest2 ,dest3]

   
   return render(request,'index.html')

def dest(request):
   # fetch data into dbms
   dests=Destination.objects.all()
   return render(request,'destination.html',{'dests':dests})

def details(request):
   dests=Destination.objects.all()
   return render(request,'details.html',{'dests':dests})