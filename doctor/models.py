from django.db import models
from django.db import models
from django.contrib.auth.models  import User
from django.db.models.signals import post_save
# from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

SPECIALITIES=(
	('der','Dermatologist'),
	('dentist','Dentist'),
    ('Psy','Psychiatrist'),
	('Pediatrician','Pediatrician'),
	('Neo','Neurologist'),
	('orth','Orthopedist'),
	('Gynec','Gynecologist'),
	('ENT','ENT Doctor'),
	('Card','Cardiologist'),
	('Intern','Internist'),
	('Optha','Ophthalmologist'),
	('Uro','Urologist'),
	('PLastic','Plastic Surgeon'),
	('Scan','Scan Center'),
	)

class Doctor(models.Model):
	name 		   = models.CharField(max_length=100,blank=True,null=True)
	title 		   = models.CharField(max_length=120,blank=True,null=True)
	description    = models.TextField(blank=True,null=True)
	speciality     = models.CharField(choices=SPECIALITIES, max_length=120,blank=True,null=True)
	clinic_address = models.CharField(max_length=150,blank=True,null=True)
	phone_number   = PhoneNumberField()
	booking_days   = models.DateField(blank=False,null=False)
	checkup_price  = models.DecimalField(decimal_places=2,max_digits=4,blank=True,null=True)
	country        = CountryField(blank_label='(select country)',blank=True)

	def __str__(self):
		return self.name 

class Patient(models.Model):
	name       = models.CharField(max_length=50,blank=True,null=True)
	age        = models.IntegerField()
	birth_date = models.DateField()

	def __str__(self):
		return self.name

class Appointment(models.Model):
	doctor 		  = models.ForeignKey(Doctor,related_name='appointment_doctor',on_delete=models.CASCADE)
	booking_days  = models.DateField(blank=False,null=False)
	booking_time  = models.DateTimeField(blank=False,null=False)
	# checkup_price = models.DecimalField(decimal_places=2,max_digits=4,blank=True,null=True)

	# def __str__(self):
	# 	return self.doctor.name

class Booking(models.Model):
	doctor 		= models.ForeignKey(Doctor,related_name='booking_doctor',on_delete=models.CASCADE)
	patient 	= models.ForeignKey(User,related_name='booking_patient',on_delete=models.CASCADE,null=True)
	appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.patient

class Attendance(models.Model):
	patient   = models.ForeignKey(Patient, related_name='attendance_patient', on_delete=models.CASCADE)
	is_attend = models.BooleanField()
	booking   = models.ForeignKey(Booking, related_name='attendance_booking', on_delete=models.CASCADE)

	def __str__(self):
		return self.patient
class Payment(models.Model):
	patient = models.ForeignKey(Patient, related_name='payment_patient',on_delete=models.CASCADE)
	cash    = models.IntegerField()
	other   = models.CharField(max_length=100)

class Comment(models.Model):
	comment 	= models.TextField(max_length=200)
	patient     = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE,null=True)
	doctor      = models.ForeignKey(Doctor, related_name='comment_on', on_delete=models.CASCADE,null=True)
	date_posted = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.doctor
