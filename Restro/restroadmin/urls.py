from django.urls import path
from . import views
urlpatterns = [
		path('login/',views.login),    
		path('dashboard/',views.dashboard),
		path('logout/',views.logout),
		path('order-detail/<int:id>',views.order_detail),
		path('notification',views.notification),
		path('orders/',views.orders),
]