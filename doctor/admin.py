from django.contrib import admin
from .models import (Doctor,
					Booking,
					Comment,
					)
admin.site.register(Doctor)

admin.site.register(Booking)
admin.site.register(Comment)