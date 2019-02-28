from rest_framework import serializers
from .models import Trip, Users
from rest_framework import viewsets

class TripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('driver_name','reg_number', 'opening_milage', 'closing_milage', 'destination', 'comments', 'distance', 'date')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'name')

