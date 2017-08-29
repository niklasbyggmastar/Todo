from django.conf.urls import url
from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new'),
    url(r'^delete/(?P<todo_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^toggle_done/(?P<todo_id>[0-9]+)/$', views.toggle_done, name='toggle_done'),
    url(r'^update/(?P<todo_id>[0-9]+)/$', views.update, name='update'),
    url(r'^comment/(?P<todo_id>[0-9]+)/$', views.comment, name='comment'),

]
