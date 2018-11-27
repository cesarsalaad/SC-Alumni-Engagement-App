#	urls.py
#
#	This file allows us to link urls to our
#	defined views so we can reference the
#	view functions in other pages
#
#	More explanation in mysite/urls.py

from django.conf.urls import url
from events import views
from django.urls import path
from django.conf.urls import include, url
urlpatterns = [
	url(r'^alumni/$',views.display_events),
	url(r'^rsvp/$',views.rsvp),
    url(r'^eventDetail/$',views.eventDetail),
    url(r'^verify/$',views.verify),
	url(r'^add_event/$',views.add_event),
]
