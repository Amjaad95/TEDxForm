from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.handl_regesteration, name='handl_regesteration'),
    url(r'^thanks/$', TemplateView.as_view(template_name='thanks.html'), name="thanks"),
    url(r'^list/$', views.list_regesteration_participants, name='list_regesteration_participants'),

]
