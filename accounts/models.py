from django.db import models
from django.contrib.auth.models  import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
        

class UserProfile(models.Model):
    username      = models.CharField(max_length=10,null=True)
    email         = models.EmailField(null=True)
    phone_number  = models.CharField(max_length=11)
    user  		  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',blank=True)
    title 		  = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    description   = models.TextField(max_length=250)
    address 	  = models.CharField(max_length=50)
    phone_number  = models.CharField(max_length=11)
    city 		  = models.CharField(max_length=20)
    photo 		  = models.ImageField(upload_to='uploads', blank=True)
    country       = CountryField(blank_label='(select country)',blank=True)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created , **kwargs):
	if created:
		UserProfile.objects.create(user=instance) #if user created create aprofile for him

# @receiver(post_save, sender=UserProfile)
# def save_profile(sender, instance, **kwargs):
# 	instance.user.save() #save user profile


