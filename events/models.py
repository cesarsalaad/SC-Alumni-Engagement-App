from django.db import models
import datetime

# Create your models here.

STATUS_CHOICES = (
	('p', 'Pending'),
	('a','Approved'),
)
class Person(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	#custom_id = models.IntegerField(blank=True, null=True)
	# attendees = models.CharField(max_length=256, default='SOME STRING')
	class_year = models.CharField(max_length=4)
	checkedIn = models.IntegerField(default=0)
	graduation = models.CharField(max_length=50,default='')
	major = models.CharField(max_length=50,default='')

	def __str__(self):
		return self.first_name

class Event(models.Model):
	numberAttendees = models.IntegerField(default=0)
	#id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	# host = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='+')
	location = models.CharField(max_length=100, null=True)
	date = models.DateField(("Date"), default=datetime.date.today)
	description = models.TextField()
	time = models.TimeField(blank=True, null=True)
	attendees = models.ManyToManyField('Person', blank=True, null=False, related_name='event')
	numberAttendees = models.IntegerField(default=0)
	status = models.CharField(max_length=1, default='a', choices=STATUS_CHOICES)

	host_first_name = models.CharField(max_length=50,default='')
	host_last_name = models.CharField(max_length=50,default='')
	host_major = models.CharField(max_length=50,default='')
	host_graduation = models.CharField(max_length=50,default='')


	def __str__(self):
		return self.title
	def approve(modeladmin, request, queryset):
		queryset.update(status='a')
	approve.short_description = "Approve selected events"
