from django.urls import path
from apps.produtos import views

app_name = "planos"

urlpatterns = [
    path('', views.PlanoList.as_view()),
    path('<int:pk>/', views.PlanoDetail.as_view()),
]