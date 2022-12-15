from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^Alunos/$', views.AlunosView.as_view(),
name='Alunos'),
]