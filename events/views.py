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
    		if request.POST.get('firstname') and request.POST.get('lastname'):
        		person=Person()
        		person.first_name= request.POST.get('firstname')
        		person.last_name= request.POST.get('lastname')
        		person.save()
			event=Event()
			event.Person = person
			return render(request, 'events/rsvp.html')  

