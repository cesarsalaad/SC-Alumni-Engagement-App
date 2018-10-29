from django.db import models

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	date = models.DateField()
	description = models.TextField()
	time = models.TimeField()
	
	def __str__(self):
		return self.title 
