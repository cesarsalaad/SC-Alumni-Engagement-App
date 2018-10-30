from django.conf.urls import url
from events import views
from django.urls import path

urlpatterns = [
    url(r'^search-form/$', views.search_form),
	url(r'^alumni/$',views.display_events),
	url(r'^rsvp/$',views.rsvp),
]
