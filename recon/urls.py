from django.urls import path
from . import views
urlpatterns=[
    path('',views.home, name='home'),
    path('accounts/',views.accounts, name='accounts'),
    path('accounttypes/',views.accounttypes, name='accounttypes'),
    path('create-accounttype/',views.createAccountTYpe, name='create-accounttype'),
    path('create-account/',views.createAccount, name='create-account'),
    path('update-account/<str:pk>/',views.updateAccount, name='update-account'),
    path('update-accounttype/<str:pk>/',views.updateAccounttype, name='update-accounttype'),
    path('delete-accounttype/<str:pk>/',views.deleteAccounttype, name='delete-accounttype'),
    path('delete-account/<str:pk>/',views.deleteAccount, name='delete-account'),
    path('transactions/',views.transactions, name='transactions'),
    path('update-transaction/<str:pk>/',views.updateTransaction, name='update-transaction'),
    path('delete-transaction/<str:pk>/',views.deleteTransaction, name='delete-transaction'),
    path('create-transaction/',views.createTransaction, name='create-transaction'),
    path('create-txntype/',views.createTxntype, name='create-txntype'),
    path('txntypes/',views.txntypes, name='txntypes'),
    path('update-txntype/<str:pk>/',views.updateTxnType, name='update-txntype'),
    path('delete-txntype/<str:pk>/',views.deleteTxnType, name='delete-txntype'),
]