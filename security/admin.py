from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(EncryptionAlgorithm)

admin.site.register(BusinessAudit)

admin.site.register(LoginAudit)

admin.site.register(PayAudit)

#admin.site.register(EncryptionAlgorithm, LoginAudit)

#admin.site.register(BusinessAudit, PayAudit)