from django.db import models
from account.models import Profile,Address
class City(models.Model):
	name=models.CharField(max_length=30)
	def __str__(self):
		return self.name+" "+str(self.id)

class Location(models.Model):
	name=models.CharField(max_length=30)
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	def __str__(self):
		return self.name+" "+str(self.id)

class Restro(models.Model):
	name=models.CharField(max_length=50)
	desc=models.TextField()
	rating=models.FloatField(
		choices=((3.2,3.2),(3.5,3.5),(3.7,3.7),(3.8,3.8),(4.2,4.2),(4.4,4.4),(4.6,4.6),(4.8,4.8),(4.9,4.9))
			)
	discount=models.IntegerField(blank=True,null=True,
		choices=((30,"30%"),(40,"40%"),(50,"50%"),(60,"60%"))
		)
	price_for_two=models.IntegerField()
	pic=models.ImageField(upload_to="media/restro_img")
	type=models.CharField(max_length=20,
		choices=(("veg","veg"),("non-veg","non-veg"),("both","both"))
		)
	open_time=models.TimeField()
	close_time=models.TimeField()
	location=models.ForeignKey(Location,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id)+self.name+" "+self.location.name+" "+self.location.city.name

class Category(models.Model):
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name

class RestroItem(models.Model):
	name=models.CharField(max_length=30)
	label=models.CharField(max_length=20,
		choices=(("Best Seller","Best Seller"),("Must Try","Must Try")),blank=True,null=True
		)
	price=models.IntegerField()
	pic=models.ImageField(upload_to="media/restro_item_img")
	restro=models.ForeignKey(Restro,on_delete=models.CASCADE)
	category=models.CharField(max_length=20)
	type=models.CharField(max_length=10,default="veg",
		choices=(("veg","veg"),("non-veg","non-veg"))
		)
	def __str__(self):
		return self.name+" "+self.restro.name

class Order(models.Model):
	profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
	date_time=models.DateTimeField(auto_now_add=True)
	address=models.ForeignKey(Address,on_delete=models.CASCADE)
	ordered=models.BooleanField(default=False)
	cancelled=models.BooleanField(default=False)
	def __str__(self):
		return str(self.id)+self.profile.user.username

class OrderItem(models.Model):
	orders_id=models.IntegerField()
	item=models.ForeignKey(RestroItem,on_delete=models.CASCADE)
	qty=models.IntegerField()
	order=models.ForeignKey(Order,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.orders_id)+self.item.name+" "+self.item.restro.name

class OrderUpdate(models.Model): # move to restroadmin app.models
	#orders_id=models.IntegerField()
	order=models.ForeignKey(Order,on_delete=models.CASCADE)
	status=models.CharField(max_length=100,choices=(
		("Order Confirmed","Order Confirmed"),("Order Cancelled","Order Cancelled"),
		("Order Being Prepared","Order Being Prepared"),("Order Pickup","Order Pickup"),
		("Order Delivered","Order Delivered")
		),blank=True,null=True)
	date_time=models.DateTimeField(auto_now_add=True)
	desc=models.TextField(blank=True,null=True)