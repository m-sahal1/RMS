from django.contrib import admin
from .models import StoreActivity, StoreBusinessHours, StoreTimezone
# Register your models here.
admin.site.register(StoreActivity)
admin.site.register(StoreTimezone)
admin.site.register(StoreBusinessHours)