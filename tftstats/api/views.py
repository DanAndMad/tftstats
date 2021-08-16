from django.shortcuts import render
from rest_framework import generics
# from .serializers import mySerializer
# from .models import myModel

# Create your views here.
def main(request):
    return render(request, "test")