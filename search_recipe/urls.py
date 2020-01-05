from . import views
from django.urls import path
from django.conf.urls import url
from recipe_home.views import log_out


urlpatterns = [
    url(r'recipe_detail/(?P<id>\d+)$',views.recipe_detail,name='recipe_detail'),
    url(r'log_out$',log_out,name='home'),
    url(r'',views.search_recipe,name='search_recipe'),

]
