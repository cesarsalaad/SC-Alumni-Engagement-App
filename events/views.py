from django.shortcuts import render
from django.http import HttpResponse 
from events.models import Event
from events.models import Person
# Create your views here.
def display_events(request):
	events = Event.objects.all()
	args = {'events':events}
	return render(request, 'events/display_events.html',args)
def search_form(request): 
	return render(request, 'events/search_form.html')

def rsvp(request):
	if request.method == 'POST':
		if request.POST.get('first_name') and request.POST.get('last_name'):
			person=Person()
			person.first_name= request.POST.get('first_name')
			person.last_name= request.POST.get('last_name')
			person.save()
			event=Event.objects.all()
			event.attendees.add(person)
			event.save()
			
			
			return render(request, 'events/rsvp.html')  
		else:
			return render(request, 'events/rsvp.html')

