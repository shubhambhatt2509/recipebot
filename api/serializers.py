from rest_framework import serializers
from . import models
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('name', 'amount', 'measurement')

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = models.Recipe
        fields = ('slug', 'name', 'description', 'cooking_instructions',
            'cooking_time', 'preparation_time',
            'created', 'modified')