from django.conf.urls import url
from events import views

urlpatterns = [
    url(r'^search-form/$', views.search_form),
]
