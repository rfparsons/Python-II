from django.db import models

# Create your models here.

class to_do_item(models.Model):
    who_added = models.CharField(max_length=200)
    who_assigned = models.CharField(max_length=200)
    add_date = models.DateTimeField('created date')
    to_do_name = models.CharField(max_length = 500)
    due_date = models.DateTimeField('due date')
    completed = models.IntegerField(default=0)