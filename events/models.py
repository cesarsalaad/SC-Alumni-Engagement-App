from django.db import models
import datetime

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	#custom_id = models.IntegerField(blank=True, null=True)
	# attendees = models.CharField(max_length=256, default='SOME STRING')

	def __str__(self):
		return self.first_name

class Event(models.Model):
	#id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	# host = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='+')
	location = models.CharField(max_length=100, null=True)
	date = models.DateField(("Date"), default=datetime.date.today)
	description = models.TextField()
	time = models.TimeField(blank=True, null=True)
	attendees = models.ManyToManyField('Person', blank=True, null=False, related_name='event')
	
	def __str__(self):
		return self.title


