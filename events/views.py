from django.shortcuts import render
from django.http import HttpResponse 
from events.models import Event
from events.model import Person
# Create your views here.
def display_events(request):
	events = Event.objects.all()
	args = {'events':events}
	return render(request, 'events/display_events.html',args)
def search_form(request): 
	return render(request, 'events/search_form.html')
def rsvp(request):
	attendees = Event.attendees.all()
