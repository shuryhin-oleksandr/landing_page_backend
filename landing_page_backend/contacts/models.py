from django.db import models


class Project(models.Model):
    class ProjectType(models.TextChoices):
        PREVIOUS = 'previous'
        ONGOING = 'ongoing'

    project_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    size = models.IntegerField()
    project_type = models.CharField(max_length=32, choices=ProjectType.choices)
    date_of_completion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.project_name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
