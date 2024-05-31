from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.clientes.urls', namespace='clientes')),
    path('produtos/', include('apps.produtos.urls', namespace='produtos'))
]
