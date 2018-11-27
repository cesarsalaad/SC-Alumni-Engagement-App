from django.contrib import admin
from events.models import Event#, Person
from django.contrib.admin.views.main import ChangeList

# Change heading on user control
from django.contrib.auth.apps import AuthConfig
AuthConfig.verbose_name = ("Manage Alumni Office Users")

# Remove user groups, we don't need them in this application
from django.contrib.auth.models import Group
admin.site.unregister(Group)


class EventAdmin(admin.ModelAdmin):
	list_display =('title','date','status',)
	actions = ['approve']
	# search_fields=('title','location')
	fields = ['title', 'location', 'date', 'time', 'description', 'host_first_name', 'host_last_name', 'host_graduation','host_major','numberAttendees']
	list_filter=('status',('date', DateFieldListFilter))

	def Attendees(self, obj):
		return ", ".join([p.first_name for p in obj.attendees.all()])

	def approve(self, request, queryset):
		queryset.update(status='a')
	approve.short_description = "Approve selected events"

admin.site.register(Event, EventAdmin)
# admin.site.register(Person)
admin.site.site_header="SCU Alumni Events"
