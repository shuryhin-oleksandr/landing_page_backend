import csv

from contacts.models import Contact

from datetime import date, timedelta

date = date.today()
one_week_ago = date - timedelta(days=7)


def export_contacts_to_csv_file(file_name):
    contacts = Contact.objects.filter(created__gte=one_week_ago)

    contacts_data = contacts.values_list('name', 'email', 'number', 'message')

    with open(f'contacts/reports/{file_name}', 'w', newline='') as file:
        header = ['name', 'email', 'number', 'message']
        write = csv.writer(file)
        write.writerow(header)
        for contact in contacts_data:
            write.writerow(contact)

    return file.name
