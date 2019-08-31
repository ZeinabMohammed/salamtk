from rest_framework import serializers
from .models import Doctor, Booking, Comment


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Doctor
		fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Booking
		fields = '__all__'
 

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Comment
		fields = '__all__'