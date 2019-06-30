from django.conf.urls import url, include

from polls import views

urlpatterns = [
    url(r'^$', views.polls, name='polls'),
url(r'^text/', views.text, name='text'),
url(r'^objects/', views.objects, name='objects'),
]