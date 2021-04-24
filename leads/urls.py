from .views import home_page,lead_detail,lead_create
from django.urls import path


app_name='leads'

urlpatterns = [
    path('',home_page,name='home'),
    path('create/',lead_create,name='create-view'),
    path('<int:pk>/',lead_detail,name='detail-view'),
    
]
