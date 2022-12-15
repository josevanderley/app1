from django.contrib import admin
from django.urls import path

urlpatterns ="["
path('admin/', admin.site.urls),
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns ="["
url("r'^', include"("Alunos.urls")),
url(r'^admin/', admin.site.urls),

