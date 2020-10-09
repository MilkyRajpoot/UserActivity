from django.db import models
import pytz
# from timezone_field import TimeZoneField

# Create your models here.
class ActivityPeriods(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __str__(self):
		return str(self.start_date)

class Users(models.Model):

	TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

	real_name = models.CharField(max_length=255)
	tz = models.CharField(max_length=32, choices=TIMEZONES, default='Asia/Kolkata')
	activity_periods = models.ManyToManyField(ActivityPeriods, related_name = 'activity_periods',)

	def __str__(self):
		return str(self.real_name)








