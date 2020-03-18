from django.db import models
from django.contrib.auth.models import User
from foodie.models import Restro,Order

# Create your models here.
class RestroProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	tel=models.IntegerField()
	restro=models.OneToOneField(Restro,on_delete=models.CASCADE)
	#pic=models.ImageField(upload_to="media/account/user_img",default="")
	def __str__(self):
		return str(self.restro.id)+" "+self.user.username

class OrderReceived(models.Model):
	restro_profile=models.ForeignKey(RestroProfile,on_delete=models.CASCADE)
	order=models.ForeignKey(Order,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id)+self.order.profile.user.username+" "+self.restro_profile.restro.name+str(self.order.ordered)+str(self.order.cancelled)

class Notification(models.Model):
	name=models.CharField(max_length=100)
	order_received=models.ForeignKey(OrderReceived,on_delete=models.CASCADE)
	def __str__(self):
		return self.name