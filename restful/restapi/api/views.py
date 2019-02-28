from django.shortcuts import render
from rest_framework import viewsets
from .models import Trip, Users
from .serializers import TripSerializers, UserSerializers

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializers

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers



# Create your views here.
