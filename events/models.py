from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.title 

class Event(models.Model):
	title = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	date = models.DateField()
	description = models.TextField()
	time = models.TimeField()
	attendees = models.ManyToManyField(Person)
	#attendance = models.IntegerField(0)
	
	def __str__(self):
		return self.title 


