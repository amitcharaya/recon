from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Account)
admin.site.register(models.Transaction)
admin.site.register(models.TxnType)
admin.site.register(models.AccountType)
admin.site.register(models.ReconDate)
admin.site.register(models.Description_NTSL)
admin.site.register(models.NTSL)
admin.site.register(models.NTSL_Dispute_Adjustments)
admin.site.register(models.RGCS)
admin.site.register(models.Channel)
admin.site.register(models.TransactionType)
admin.site.register(models.TransactionCycle)
admin.site.register(models.Status)
admin.site.register(models.InwardOutward)