from django.conf.urls import url
from events import views
from django.urls import path
from django.conf.urls import include, url
urlpatterns = [
    url(r'^search-form/$', views.search_form),
	url(r'^alumni/$',views.display_events),
	url(r'^rsvp/$',views.rsvp),
    url(r'^eventDetail/$',views.eventDetail),
    url(r'^verify/$',views.verify),
	url(r'^add_event/$',views.add_event),
]
