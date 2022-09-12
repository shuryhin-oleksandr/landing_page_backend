from django.urls import path

from contacts.views import ContactAPIView, PreviousProjectsView, OngoingProjectView

urlpatterns = [
    path('api/v1/contacts/', ContactAPIView.as_view(), name='contacts'),
    path('api/v1/ongoing-projects/', OngoingProjectView.as_view(), name='ongoing_projects'),
    path('api/v1/previous-projects/', PreviousProjectsView.as_view(), name='previous_projects'),
]