from django.contrib import admin
from .models import City,Location,Restro,RestroItem,Order,Category,OrderItem,OrderUpdate
# Register your models here.
admin.site.register(City)
admin.site.register(Location)
admin.site.register(Restro)
admin.site.register(RestroItem)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(OrderUpdate)
