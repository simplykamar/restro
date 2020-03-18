from django.contrib.auth.models import User
from .models import RestroProfile

class CustomEmailIDBackend(object):
	def authenticate(self,req,restro_id=None,username=None,password=None):
		try:
			restro_profile=RestroProfile.objects.get(restro__id=restro_id,user__email=username)
			if restro_profile.user.check_password(password):
				return restro_profile.user
			return None
		except:
			return None
	def get_user(self,user_id):
		try:
			return User.objects.get(pk=user_id)
		except:
			return None

class CustomTelIDBackend(object):
	def authenticate(self,req,restro_id=None,username=None,password=None):
		try:
			restro_profile=RestroProfile.objects.get(restro__id=restro_id,tel=username)
			if restro_profile.user.check_password(password):
				return restro_profile.user
			return None
		except:
			return None
	def get_user(self,user_id):
		try:
			return User.objects.get(pk=user_id)
		except:
			return None
