from django.views import View
from django.urls import resolve
from onlineapp.models import *
from django.shortcuts import  render,redirect
from onlineapp.forms import *
from  django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.models import User
def logout_user(request):
    logout(request)
    return redirect('login_url')

class loginview(View):
    def get(self,request,*args,**kwargs):
        form=loginform()
        return render(request,'index1.html',context={'form':form})
    def post(self,request,*args,**kwargs):
        user=authenticate(request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request,user)
            return redirect("season_html",2019)

class signupview(View):
    def get(self,request,*args,**kwargs):
        form=signupform()
        return render(request,'index2.html',context={'form':form})
    def post(self,request,*args,**kwargs):
        form=signupform(request.POST)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            user.save()
            if user is not None:
                login(request, user)
                return redirect("season_html",2019)


