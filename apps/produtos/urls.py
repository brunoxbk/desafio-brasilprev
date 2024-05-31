from django.urls import path
from apps.produtos import views

app_name = "produtos"

urlpatterns = [
    path('', views.ProdutoList.as_view()),
    path('<int:pk>/', views.ProdutoDetail.as_view())
]