from django.db import models

# Create your models here.
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='candidate_photos/', blank=True, null=True)


    def __str__(self):
        return self.name

