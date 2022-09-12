from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView, ListAPIView
from contacts.models import Contact, Project
from contacts.serializers import ContactSerializer, PreviousProjectSerializer, OngoingProjectSerializer
from landing_page_backend.settings import EMAIL_HOST_USER


class ContactAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        send_mail(
            'Feedback from the contact form',
            'Thank you for your interest, we will contact you within 48 hours',
            EMAIL_HOST_USER,
            [f'{email}'],
            fail_silently=False,
        )


class PreviousProjectsView(ListAPIView):
    queryset = Project.objects.filter(project_type=Project.ProjectType.PREVIOUS)
    serializer_class = PreviousProjectSerializer


class OngoingProjectView(ListAPIView):
    queryset = Project.objects.filter(project_type=Project.ProjectType.ONGOING)
    serializer_class = OngoingProjectSerializer
