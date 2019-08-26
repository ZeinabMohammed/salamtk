from django.db import models
from django.db import models
from django.contrib.auth.models  import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField


class Doctor(models.Model):
	name 		   = models.CharField(max_length=100,blank=True,null=True)
	title 		   = models.CharField(max_length=120,blank=True,null=True)
	description    = models.TextField(blank=True,null=True)
	specialization = models.CharField(max_length=120,blank=True,null=True)
	clinic_address = models.CharField(max_length=150,blank=True,null=True)
	phone_number   = PhoneNumberField()
	checkup_price  = models.DecimalField(decimal_places=2,max_digits=4,blank=True,null=True)
	country        = CountryField(blank_label='(select country)',blank=True)


	def __str__(self):
		return self.name

class Booking(models.Model):
	doctor 			= models.ForeignKey(Doctor,related_name='doctor',on_delete=models.CASCADE)
	client 			= models.ForeignKey(User,related_name='client',on_delete=models.CASCADE)
	checkup_date 	= models.DateField(blank=False,null=False)
	checkup_time    = models.DateTimeField(blank=False,null=False)


class Comment(models.Model):
	comment 	= models.TextField(max_length=200)
	user 	    = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
	doctor      = models.ForeignKey(Doctor, related_name='comment_on', on_delete=models.CASCADE)
	date_posted = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user
