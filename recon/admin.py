from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Account)
admin.site.register(models.Transaction)
admin.site.register(models.TxnType)
admin.site.register(models.AccountType)