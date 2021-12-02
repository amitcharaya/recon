from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name='home'),
    path('create-accounttype/',views.createAccountTYpe, name='create-accounttype'),
    path('create-account/',views.createAccount, name='create-account'),
    path('create-transaction/',views.createTransaction, name='create-transaction'),
    path('create-txntype/',views.createTxntype, name='create-txntype')
]