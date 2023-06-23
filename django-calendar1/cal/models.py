from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Dsensor(models.Model):
    time = models.CharField(primary_key=True,max_length=10)
    humi = models.FloatField()
    tem = models.FloatField()
    
    class Meta:
        db_table = "dsensor"



class User(models.Model):
    time = models.CharField(primary_key=True, max_length=10)
    user = models.CharField(max_length=10)

    class Meta:
        db_table = "user_data"
