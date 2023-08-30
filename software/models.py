from django.db import models
from django.urls import reverse

class Software(models.Model):
    company_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    software_username = models.CharField(max_length=100)
    expiration_date = models.DateField()
    version = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name


    def get_absolute_url(self):
        return reverse('software_edit', kwargs={'pk': self.pk})