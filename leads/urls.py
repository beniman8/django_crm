from .views import home_page,lead_detail,lead_create,lead_update
from django.urls import path


app_name='leads'

urlpatterns = [
    path('',home_page,name='home'),
    path('create/',lead_create,name='create-view'),
    path('<int:pk>/',lead_detail,name='detail-view'),
    path('<int:pk>/update/',lead_update,name='update-view'),
    
]
