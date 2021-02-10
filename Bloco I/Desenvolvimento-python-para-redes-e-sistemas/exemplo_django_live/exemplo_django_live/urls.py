from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('gerenciador_de_tarefas.urls')),
    path('admin/', admin.site.urls),
]
