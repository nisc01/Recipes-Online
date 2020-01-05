from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    url(r'recipe_add',views.recipe_add,name='recipe_add'),
    url(r'modify_recipe/(?P<id_>\w+)$',views.modify_recipe, name = 'modify_recipe'),
    url(r'delete_recipe/(?P<id_>\w+)$',views.delete_recipe, name = 'modify_recipe'),
    url(r'log_out$',views.log_outt, name = 'log_out'),
    url(r'', views.your_recipe, name = 'your_recipe'),

]
