from rest_framework import viewsets
from .serializer import exp1Serializer, exp2Serializer
from .models import exp1, exp2
from django_filters.rest_framework import DjangoFilterBackend

class exp1Viewset(viewsets.ModelViewSet):
    queryset = exp1.objects.all()
    serializer_class = exp1Serializer
    filter_backends = (DjangoFilterBackend,) 
    filter_fields = ['geneName']

class exp2Viewset(viewsets.ModelViewSet):
    queryset = exp2.objects.all()
    serializer_class = exp2Serializer
    filter_backends = (DjangoFilterBackend,) 
    filter_fields = ['geneName']

# Create your views here.
