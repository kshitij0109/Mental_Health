from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=60)
    Date = models.DateTimeField(auto_created=True)
    Time = models.TimeField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.Name} - {self.email}'
