#	views.py
#
#	Views are Django's way of managing
# 	functions that take in requests
# 	and return responses
#

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from events.models import Event
from events.models import Person

# Create your views here
def display_events(request):
	events = Event.objects.filter(status='a')
	args = {'events':events}
	return render(request, 'events/display_events.html',args)

def rsvp(request):
	# people = Event.objects.all()[0]

	# people = list(people.attendees.all())

	events = list(Event.objects.filter(status='a'))

	if request.method == 'POST':
		for event in events:
			# , graduation=request.POST.get('class_year')
			if request.POST.get('first_name') and request.POST.get('last_name') and str(event.id) == request.POST.get('id'):
				person=Person.objects.create(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), graduation=request.POST.get('class_year'), major=request.POST.get('major'))
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
		# person=Person.objects.create(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), class_year=request.POST.get('class_year'))
		# , host_first_name=request.POST.get('first_name'), host_last_name=request.POST.get('last_name'), status='p', host_major=request.POST.get('class_year')
		events=Event.objects.create(host_first_name=request.POST.get('first_name'), host_last_name=request.POST.get('last_name'), host_graduation=request.POST.get('class_year'),host_major=request.POST.get('major'),title=request.POST.get('title'), location=request.POST.get('location'), date=request.POST.get('date'), description=request.POST.get('description'), time=request.POST.get('time'), status='p')
		events.save()
		return HttpResponseRedirect('/alumni')



def eventDetail(request):
	events = list(Event.objects.filter(status='a'))

	if request.method == 'POST':
		for event in events:
			if str(event.id) == request.POST.get('id'):

				event.numberAttendees = event.numberAttendees+1
				index = -1
				for i in events:
					index+=1
					if i.id == event.id:
						people = events[index].attendees.all()
						break;
				verified = []
				for i in people:
					if i.checkedIn == 0:
						verified.append(i)
				event.save()


				args = {'people':people, 'event':event}

				return render(request, 'events/eventDetail.html',args)


def verify(request):
	events = list(Event.objects.filter(status='a'))
	persons = Person.objects.all()

	if request.method == 'POST':
		for event in events:
			if str(event.id) == request.POST.get('eventid'):
				event.numberAttendees = event.numberAttendees+1
				event.save()
		for person in persons:
			if str(person.id) == request.POST.get('id'):
				person.checkedIn = 1
				person.save()
				return HttpResponseRedirect('/alumni')
