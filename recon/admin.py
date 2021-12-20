from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.
class AccountResource(resources.ModelResource):
    class Meta:
        model=models.Account

@admin.register(models.Account)
class AccountAdmin(ImportExportModelAdmin):
    pass

@admin.register(models.Transaction)
class TransactionResource(ImportExportModelAdmin):
    pass

@admin.register(models.TxnType)
class TransactionTypeResource(ImportExportModelAdmin):
    pass

@admin.register(models.AccountType)
class AccountTypeResource(ImportExportModelAdmin):
    pass


admin.site.register(models.ReconDate)

@admin.register(models.Description_NTSL)
class DescriptionNTSLResource(ImportExportModelAdmin):
    pass


admin.site.register(models.NTSL)
admin.site.register(models.NTSL_Dispute_Adjustments)
admin.site.register(models.RGCS)

@admin.register(models.Channel)
class ChannelResource(ImportExportModelAdmin):
    pass

@admin.register(models.TransactionType)
class TransactionTypeResource(ImportExportModelAdmin):
    pass

@admin.register(models.TransactionCycle)
class TransaactionCycleResource(ImportExportModelAdmin):
    pass

@admin.register(models.Status)
class StatusResource(ImportExportModelAdmin):
    pass

@admin.register(models.InwardOutward)
class InwardOutwardResource(ImportExportModelAdmin):
    pass
