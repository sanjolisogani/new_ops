from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming_soon, name = 'coming_soon'),
    path('email',views.email,name='email'),
]
