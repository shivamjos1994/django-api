from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', views.api, name="api"),
    path('apiOne/<int:id>/', views.apiOne, name="apiOne")
]
