from django.urls import path

urlpatterns = [
    path('recipes', views.recipe_list)
]