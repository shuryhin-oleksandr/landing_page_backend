from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
from datetime import date
from contacts.utils import export_contacts_to_csv_file
from landing_page_backend.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT

today = date.today()


class Command(BaseCommand):
    help = 'Exports previous week contact to a file and sends an email with a report file attached to an administrator.'

    def handle(self, *args, **options):
        file_name = f'contacts-{today}.csv'
        path = export_contacts_to_csv_file(file_name)

        message = 'Weekly reports'
        subject = 'This is weekly reports'
        email = EmailMessage(subject, message, EMAIL_HOST_USER, [EMAIL_RECIPIENT])
        file = open(path, 'r')
        email.attach(file_name, file.read())
        email.send()
