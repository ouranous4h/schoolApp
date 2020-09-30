from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# def index(request):
#   #return HttpResponse("Hello World!")
#   return render(request, "authenticate/index.html")

### register routine
def register(request):
  return render(request, "authenticate/register.html")

### login routine
def login(request):
  return render(request, "authenticate/login.html")

### logout routine
def logout(request):
  return HttpResponseRedirect(reverse("authenticate:login"))