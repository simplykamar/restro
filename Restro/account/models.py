from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	tel=models.IntegerField()
	#pic=models.ImageField(upload_to="media/account/user_img",default="")
	def __str__(self):
		return self.user.username

class Favourite(models.Model):
	restro_id=models.IntegerField()
	profile=models.ForeignKey(Profile,models.CASCADE)
	def __str__(self):
		return str(self.restro_id)
		
class Address(models.Model):
	address=models.TextField()
	area=models.CharField(max_length=100)
	landmark=models.CharField(max_length=50)
	tag=models.CharField(max_length=5,
		choices=(("home","home"),("work","work"),("other","other"))
		)
	profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
	def __str__(self):
		return self.area+" "+self.tag
