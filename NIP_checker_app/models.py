from django.db import models

# Create your models here.
class NIP(models.Model):
    nip_number = models.CharField(max_length=10, unique=True)
    result_from_MF = models.CharField(max_length=128)
    #add_date = models.DateTimeField(auto_now_add=True)
    add_date = models.DateTimeField(null=True)
    check_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.nip_number


