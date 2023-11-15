from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from.models import place
# Create your views here.
def demo(request):
    name = "india"
    return render(request,"home.html",{'obj':name})
def about(request):
    template= loader.get_template('about.html')
    return HttpResponse(template.render())
def index(request):
    template= loader.get_template('index.html')
    return HttpResponse(template.render())
def contact(request):
    return HttpResponse("hello am contact")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res= x+y
#     return render(request,"result.html", {'result':res})
def index(request):
    obj=place.objects.all()
    return render(request, "index.html",{'result':obj})