from django.urls import path
from apps.planos import views

app_name = "planos"

urlpatterns = [
    path('', views.PlanoList.as_view()),
    path('<int:pk>/', views.PlanoDetail.as_view()),

    path('aportes/', views.AporteList.as_view()),
    path('aportes/<int:pk>/', views.AporteDetail.as_view()),

    path('resgates/', views.ResgateList.as_view()),
    path('resgates/<int:pk>/', views.ResgateDetail.as_view()),
]