from django.urls import path
from . import views

urlpatterns = [
    path('', views.scores),
    # path('view/', views.view_scoreboard),
]
