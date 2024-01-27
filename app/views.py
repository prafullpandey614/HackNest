from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,forms,logout
from django.shortcuts import get_object_or_404

from rest_framework.generics import CreateAPIView

from app.serializers import HackathonSerializer

from .models import Hackathons

class Home(View):
    def get(self,request):
        return render(request,'app/index.html')
    
class Register(View):
    def post(self,request):
        data = request.POST
        # username = data["username"]
        # password = data["password"]
        print(data)
        form = forms.UserCreationForm(request.POST)
        print(form.is_valid())
        try:
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('home')
            else :
                return render(request,'app/register.html',context={
                "error": True,
            })
        except Exception as e:
            print("Something Occured Bad ",e)
            return render(request,'app/register.html',context={
                "error": True,
            })
    def get(self,request):
        return render(request,'app/register.html')
class Login(View):
    def post(self,request):
        data = request.POST
        username = data["username"]
        password = data["password"]
        print(data)
        try:
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect('home')
        except Exception as e:
            print("Something Occured Bad ",e)
            return render(request,'app/login.html',context={
                "error": True,
            })
    def get(self,request):
        return render(request,'app/login.html')
class Logout(View):
    def get(self,request):
        try:
            logout(request)
            return redirect('home')
        except Exception as e:
            print("Something Occured Bad ",e)
            return render(request,'app/login.html',context={
                "error": True,
            })
        
class Hackathonss(View):
    def get(self,request):

        return render(request,'app/hackathons.html')
class HackathonsList(View):
    def get(self,request):
        hackathons = Hackathons.objects.all()
        return render(request,'app/hacklist.html',context={
            "hackathon" : hackathons 
        })
class SingleHackathonView(View):
    def get(self,request):
        return render(request,'app/singlehack.html')
    
class Profile(View):
    def get(self,request):
        return render(request,'app/profileuser.html')

class AddHackathonAPIView(CreateAPIView):
    queryset = Hackathons.objects.all()
    serializer_class = HackathonSerializer
    