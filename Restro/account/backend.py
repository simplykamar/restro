from django.contrib.auth.models import User
from .models import Profile
class CustomEmailBackend(object):
	def authenticate(self,req,username=None,password=None):
		try:
			user=User.objects.get(email=username)
			if user.check_password(password):
				return user
			return None
		except User.DoesNotExist:
			return None
	def get_user(self,user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None

class CustomTelBackend(object):
	def authenticate(self,req,username=None,password=None):
		try:
			profile=Profile.objects.get(tel=username)
			if profile.user.check_password(password):
				return profile.user
			return None
		except:
			return None
	def get_user(self,user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None