from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from events.models import Event
from events.models import Person
# Create your views here.Last Name
def display_events(request):
	events = Event.objects.filter(status='a')
	args = {'events':events}
	return render(request, 'events/display_events.html',args)
def search_form(request): 
	return render(request, 'events/search_form.html')

def rsvp(request):
	# people = Event.objects.all()[0]
	
	# people = list(people.attendees.all())
              
	events = list(Event.objects.filter(status='a'))

	if request.method == 'POST':
		for event in events:
			if request.POST.get('first_name') and request.POST.get('last_name') and str(event.id) == request.POST.get('id'):
				person=Person.objects.create(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'))
				# person.first_name= request.POST.get('first_name')
				# person.last_name= request.POST.get('last_name')
				# person.first_name= event.id
				# person.last_name= request.POST.get('id')
				#person.custom_id = request.POST.get('id')
				#event = Event()	
				#event.attendees.add(person)
				person.save()
				event.attendees.add(person)

				index = -1
				for i in events:
					index+=1
					if i.id == event.id:
						people = events[index].attendees.all()
						break;
					

				args = {'people':people}
				
				return render(request, 'events/rsvp.html',args)  

def add_event(request):
	if request.method == 'POST':
		person=Person.objects.create(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), class_year=request.POST.get('class_year'))
		events=Event.objects.create(title=request.POST.get('title'), location=request.POST.get('location'), date=request.POST.get('date'), description=request.POST.get('description'), time=request.POST.get('time'), status='p')

		return HttpResponseRedirect('/alumni')






