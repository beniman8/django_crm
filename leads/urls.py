from .views import home_page,lead_detail
from django.urls import path


app_name='leads'

urlpatterns = [
    path('',home_page,name='home'),
    path('<pk>/',lead_detail,name='detail-view')
    
]
