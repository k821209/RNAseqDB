from rest_framework import serializers
from .models import exp1, exp2

class exp1Serializer(serializers.ModelSerializer):
    class Meta:
        model = exp1
        fields = ('geneName','countArray')

class exp2Serializer(serializers.ModelSerializer):
    class Meta:
        model = exp2
        fields = ('geneName','countArray')

