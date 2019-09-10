from django.contrib import admin
from .models import (Doctor,
					Booking,
					Comment,
					Patient,
					Appointment
					)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Booking)
admin.site.register(Comment)
admin.site.register(Appointment)