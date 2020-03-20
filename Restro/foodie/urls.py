from django.urls import path
from .import views
urlpatterns = [
		path('',views.index),
		path('search/',views.search),
		path('restro-view/<int:id>/',views.restro_view),
		path('checkout-step-1/',views.checkout_step_1),
		path('checkout-step-2/<int:id>',views.checkout_step_2),
		path('add-address/',views.add_address),
		path('track-order/',views.track_order),
		path('orders',views.orders),
		path('addresses',views.addresses),
		path('remove-address/<int:id>',views.delete_address),
		path('add-favourite/<int:id>',views.add_favourite),
		path('remove-favourite/<int:id>',views.delete_favourite),
		path('favourites',views.favourites),
		path('payments',views.payments),
		path('404',views.error_404),
		path('cancel-order/<int:id>',views.cancel_order),
		path('check-update/',views.check_update),
		path('location-based-restaurant/<int:id>',views.location_based_restaurant),
		path('city-based-restaurant/<int:id>',views.city_based_restaurant),
]