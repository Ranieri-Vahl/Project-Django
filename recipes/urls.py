from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('recipe/category/<int:category_id>/', views.category, name='category'),  # noqa E501
]
