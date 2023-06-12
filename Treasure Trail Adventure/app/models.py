from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    time_limit = models.DurationField(default=timezone.timedelta(minutes=1))
    award = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    options = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class UserRule(models.Model):
    Max_Award = models.IntegerField(blank=True, null=True)
    Max_questions = models.IntegerField(blank=True, null=True)

class UserScore(models.Model):
    userName=models.TextField(blank=True,null=True)
    score=models.TextField(blank=True,null=True)
    date=models.DateField(auto_now=True)