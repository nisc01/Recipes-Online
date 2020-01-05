from django.shortcuts import render,HttpResponse
from your_recipes.models import Recipes
from django.conf.urls import url
import requests

# Create your views here.
def search_recipe(request):
    recipes=Recipes()
    search_result=[]
    search_result_api=[]
    username=request.GET['username']
    searched_recipe=request.GET['searched_recipe']

    response=requests.get('http://www.recipepuppy.com/api/?i='+searched_recipe+'&q=omelet&p=3')
    api_data=response.json()
    api_data_results=api_data['results']

    search=[_.title for _ in Recipes.objects.all().filter(title__icontains=searched_recipe)]
    for j in search:
        if (searched_recipe.lower() in j.lower()) or \
                (searched_recipe in [_.ingredients for _ in Recipes.objects.all().filter(ingredients__icontains=searched_recipe)]):
            for _ in (Recipes.objects.filter(title__icontains=searched_recipe)):
                search_result.append([_.id,_.title,_.ingredients,_.image])
            for _ in (Recipes.objects.filter(ingredients__icontains=searched_recipe)):
                search_result.append([_.id,_.title,_.ingredients,_.image])

    for _ in api_data_results:
        search_result_api.append([_["href"],_['title'],_['ingredients']])

    return render(request,'search_recipe/search_result.html',
                  {'search_result':search_result,'search_result_api':search_result_api,'username':username})

def recipe_detail(request,id):
    idd=id
    recipe=Recipes.objects.get(id=idd)
    return render(request,'search_recipe/recipe_detail.html',
                  {
                   'title':recipe.title,
                   'image':recipe.image,
                   'author_name':recipe.author_name,
                   'date_posted':recipe.date_posted,
                   'ingredients':recipe.ingredients,
                   'description':recipe.description})