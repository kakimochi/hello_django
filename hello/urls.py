from django.urls import path
from . import views

from .models import LogMessage

LimitView = 5

urlpatterns = [
    path('',
        views.HomeListView.as_view(
            queryset=LogMessage.objects.order_by('-log_date')[:LimitView],
            context_object_name='message_list',
            template_name='hello/home.html',
        ), 
        name="home"
    ),
    # path('', views.home, name="home"),
    # path('hello/<name>', views.hello_there, name="hello_there"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('log/', views.log_message, name="log"),
]
