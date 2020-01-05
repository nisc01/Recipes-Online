from django.shortcuts import render,redirect
from .models import AddUser
from django.http import HttpResponseRedirect
from django.urls import reverse
from your_recipes.models import Recipes


# Create your views here.
def home(request):
    recipes=[]
    for _ in Recipes.objects.all():
        image=_.image
        recipes.append([_.title,image])
    return render(request,'recipe_home/home.html',{'recipes':recipes})

def log_out(request):
    return HttpResponseRedirect(reverse('recipe_home:home'))
    #return render(request,'recipe_home/home.html')


def sign_in(request):
    return render(request,'recipe_home/sign_in.html')

def sign_up(request):
    return render(request,'recipe_home/sign_up.html')

def add_user(request):
    users=AddUser()
    name=request.POST['username']
    password=request.POST['password']
    if name in [_.name for _ in AddUser.objects.all()]:
        message='User name already present'
        return render(request,'recipe_home/sign_up.html',{'context':message})
    else:
        users.name=name
        users.password=password
        users.save()
    return render(request,'recipe_home/search_recipe.html',{'username':name})

def user_authenticate(request):
    check_user=AddUser()
    username=request.POST['username']
    password=request.POST['password']
    if username in [_.name for _ in AddUser.objects.all()] and \
            password==AddUser.objects.all().get(name=username).password:
        return render(request,'recipe_home/search_recipe.html/',{'username':username})
    else:
        return render(request,'recipe_home/sign_in.html',{'context':'Username or password invalid'})





