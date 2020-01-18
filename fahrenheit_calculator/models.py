from django.db import models


class UserDetails(models.Model):
	""" details of User """
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=128)

class CalculatorDetails(models.Model):
	""" details of Calculator """
	user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
	celsius = models.FloatField()
	fahrenheit = models.FloatField()
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
		
