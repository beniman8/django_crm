from .views import home_page
from django.urls import path


app_name='leads'

urlpatterns = [
    path('',home_page,name='home')
    
]
