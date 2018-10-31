from django.contrib import admin
from .models import Event, Person
from django.contrib.admin.views.main import ChangeList


class EventAdmin(admin.ModelAdmin):
	list_display =('title','date', 'Attendees')
	# search_fields=('title','location')
	fields = ['title', 'location', 'date', 'time', 'description', 'attendees']

	def Attendees(self, obj):
		return ", ".join([p.first_name for p in obj.attendees.all()])

admin.site.register(Event, EventAdmin)
admin.site.register(Person)

