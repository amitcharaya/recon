from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name='home'),
    path('create-accounttype/',views.createAccountTYpe, name='create-accounttype')
]