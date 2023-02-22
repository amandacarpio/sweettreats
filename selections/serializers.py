from .models import Selections
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class SelectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Selections
        fields = ['id', 'Dessert_Name', 'Allergies', 'If_yes_please_specify', 'Dessert_Details', 'Email', 'Budget']