from django.urls import path
from . import views
urlpatterns =[
    path('',views.index , name='index'),
    path('about/',views.about , name='about'),
    path('department/',views.department , name='department'),
    path('doctors/',views.doctor , name='doctors'),
    path('booking/',views.booking , name='bookings'),
    path('contact/',views.contact , name='contact'),
]