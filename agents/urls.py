from django.urls import path
from .views import AgentsListView,AgentsCreateView

app_name='agents'

urlpatterns = [
    path('',AgentsListView.as_view(),name='agent-list'),
    path('create/',AgentsCreateView.as_view(),name='agent-create'),
    
]
