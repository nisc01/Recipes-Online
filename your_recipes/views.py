from django.shortcuts import render,HttpResponse
from .forms import RecipeAddForm
from .models import  Recipes
from recipe_home.views import log_out
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def your_recipe(request,username):
    recipes=Recipes()
    user_recipes=[]
    for _ in  Recipes.objects.filter(author_name=username):
        user_recipes.append([_.id,_.title])
    return render(request,'your_recipes/home.html',{'user_recipes':user_recipes,'username':username})




def recipe_add(request,username):
    if request.method == 'POST':
        form=RecipeAddForm(request.POST,request.FILES)
        if form.is_valid():
            edit_form=form.save(commit=False)
            edit_form.author_name=username
            edit_form.save()
            result=your_recipe(request,username)
            return result
        else:
            return HttpResponse('Form is not valid')
    else:
        form = RecipeAddForm()
        return render(request,'your_recipes/recipe_add.html',{'form':form,'username':username})
    #return render(request,'recipe_home/recipe_add.html')

def modify_recipe(request,username,id_):
    recipe_record=Recipes.objects.get(id=id_)
    if request.method=='GET':
        form=RecipeAddForm(instance=recipe_record)
        return render(request,'your_recipes/recipe_add.html',{'form':form,'username':username})
    else:
        form=RecipeAddForm(request.POST,request.FILES,instance=recipe_record)
        if form.is_valid():
            form.save()
            return HttpResponse('form modified successfully')
        else:
            print('form.errors',form.errors)
            return HttpResponse('form not modified')

def delete_recipe(request,username,id_):
    recipe_record=Recipes.objects.get(id=id_)
    recipe_record.delete()
    return HttpResponse('record deleted')

def log_outt(request,username):
    return log_out(request)