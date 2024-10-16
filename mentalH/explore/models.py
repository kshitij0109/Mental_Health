from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=60)
    Date = models.DateTimeField()
    Time = models.TimeField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    type = models.CharField(max_length=50, default='regular')
    

    def __str__(self):
        return f'{self.Name} - {self.email}'

class CounselingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    Create_at = models.DateTimeField(auto_now_add=True)
    

class CounselingQueue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(CounselingSession, on_delete=models.CASCADE)
    position = models.ImageField()
    created_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')