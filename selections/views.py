from django.shortcuts import render
from .models import Selections
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SelectionsSerializer

# Create your views here.
class SelectionsViewSet(viewsets.ModelViewSet):
    queryset = Selections.objects.all()
    serializer_class = SelectionsSerializer
    permission_classes = [permissions.AllowAny]