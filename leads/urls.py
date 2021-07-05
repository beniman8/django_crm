from .views import (home_page,
                    lead_detail,lead_create,lead_update,lead_delete,
                    HomePageView,LeadDetailView,LeadCreateView,
                    LeadUpdateView,LeadDeleteView,AssignAgentView,
                    CategoryListView,
                    )
from django.urls import path


app_name='leads'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('create/',LeadCreateView.as_view(),name='create-view'),
    path('<int:pk>/assign-agent/',AssignAgentView.as_view(),name='assign-view'),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name='update-view'),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name='delete-view'),
    path('<int:pk>/',LeadDetailView.as_view(),name='detail-view'),
    path('categories/',CategoryListView.as_view(),name='category-list'),
    
]
 