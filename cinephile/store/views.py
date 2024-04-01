from django.shortcuts import render,redirect
from django.views.generic import View
from store.forms import RegForm,LoginForm
from store.models import Category
from django.contrib.auth import authenticate,login,logout


class HomeView(View):
    def get(self,request,*args,**kwargs):
        form=Category.objects.all()
        return render(request,"home.html",{"form":form})


class RegView(View):
    def get(self, request, *args, **kwargs):
        form = RegForm()
        return render(request,"register.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("home")
        else:
            print("not saved")
            return render(request,"register.html", {'form': form})
        

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pswd)
            if user_obj:
                print("valid credential")
                login(request,user_obj)
                return redirect("home")
            else:
                print("invalid credential")
                return render(request,"login.html",{"form":form})
            

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
    