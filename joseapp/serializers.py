from rest_framework import serializers
from .models import Alunos
class AlunosSerializer(serializers.ModelSerializer):
 class Meta:
   model = Alunos
 fields = "["
'id',
'nome','endereço','email',