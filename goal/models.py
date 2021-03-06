from django.db import models
from django.contrib.auth.models import User
class Goal(models.Model):
    """Represents a single Goal"""
    description = models.TextField()
    done = models.BooleanField(default=False)
    achievement = models.ForeignKey(
        'Achievement', on_delete=models.SET_NULL, null=True)
    buddy = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return self.description
class Achievement(models.Model):
    name = models.CharField(max_length=300)
    goals = models.ManyToManyField('Goal', related_name="goals")
    buddy = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return self.name