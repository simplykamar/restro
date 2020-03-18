from django.contrib import admin
from .models import Notification,RestroProfile,OrderReceived
# Register your models here.

admin.site.register(Notification)
admin.site.register(RestroProfile)
admin.site.register(OrderReceived)
