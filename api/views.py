from django.shortcuts import render
from django.http import JsonResponse
from . import models


def recipe_list(request):
    result = []

    for recipe in Recipe.objects.all():
        result.append({'name': recipe.name, 'slug': recipe.slug})

    return JsonResponse(result)
