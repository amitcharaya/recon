from import_export import resources
from . import models

class AccountResource(resources.ModelResource):
    class Meta:
        model=models.Account