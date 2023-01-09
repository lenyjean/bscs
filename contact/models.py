from django.db import models

# Create your models here.
class ContactModel(models.Model):
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Contact'

    def __str__(self):
        return self.your_email
