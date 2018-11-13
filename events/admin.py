from django.contrib import admin
from events.models import Event, Person
from django.contrib.admin.views.main import ChangeList


class EventAdmin(admin.ModelAdmin):
	list_display =('title','date','status',)
	actions = ['approve']
	# search_fields=('title','location')
	fields = ['title', 'location', 'date', 'time', 'description', 'attendees']
	list_filter=('status',)

	def Attendees(self, obj):
		return ", ".join([p.first_name for p in obj.attendees.all()])

	def approve(self, request, queryset):
		queryset.update(status='a')
	approve.short_description = "Approve selected events"

admin.site.register(Event, EventAdmin)
admin.site.register(Person)
admin.site.site_header="SCU Alumni Events"
