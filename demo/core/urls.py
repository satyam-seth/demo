from django.urls import path
from . import views

urlpatterns=[
    path('org/',views.org,name='org'),
    path('emp/',views.emp,name='emp'),
]