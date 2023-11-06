from django.db import models

class PaymentDeets(models.Model):
	def __str__(self):
		return self.name
	
	name = models.CharField(max_length=100)
	phone_no = models.IntegerField() # number recieving payment
	amount = models.IntegerField() # amount to be paid
	
	
