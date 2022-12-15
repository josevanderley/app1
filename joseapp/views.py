from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Alunos
from .serializers import AlunosSerializer
class AlunosView(generics.ListCreateAPIView):
  queryset = Alunos.objects.all()
  serializer_class = AlunosSerializer