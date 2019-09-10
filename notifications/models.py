from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from doctor.models import Comment,Doctor

class Notification(models.Model):
	user  = models.ForeignKey(User, related_name='notification', on_delete='models.CASCADE')
	title = models.CharField(max_length=20)
	body  = models.TextField()


	def __str__(self):
		return self.user.username




# class CommentNotification(models.Model):
# 	receiver= models.ForeignKey(Doctor,on_delete='models.CASCADE',related_name='doctor_notify',null=True)
# 	comment = models.ForeignKey(Comment,on_delete='CASCADE',related_name='comment_notify')
# 	title   = models.CharField(max_length=20)
# 	body    = models.TextField()

	# def commentdoctor(self):
	# 	return self.comment.doctor
