from rest_framework import serializers
from .models import Doctor, Booking, Comment, Appointment,Patient, Attendance, Payment
from django.contrib.auth.models  import User


class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Doctor
		fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
	doctor 		= serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
	patient 	= serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
	appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())
	
	class Meta:
		model  = Booking
		fields = ['doctor','patient','appointment']

	def create(self,data):
		book = Booking.objects.create(
						doctor      = data['doctor'],
						patient 	= data['patient'],
						appointment = data['appointment'],	
					)
		book.save()
		return book
class AttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Attendance
		fields = '__all__'
		
class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Payment
		fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
	doctor 		 = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
	booking_days = serializers.DateField()
	booking_time = serializers.DateTimeField()
	# checkup_price= serializers.DecimalField(max_digits=2,decimal_places=2)
	
	class Meta:
		model  = Appointment
		fields = ['doctor','booking_days','booking_time']

	def create(self,data):
		appointment = Appointment.objects.create(
						doctor       = data['doctor'],
						booking_days = data['booking_days'],
						booking_time = data['booking_time']
					)
		appointment.save()
		return appointment
 

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Comment
		fields = '__all__'


   