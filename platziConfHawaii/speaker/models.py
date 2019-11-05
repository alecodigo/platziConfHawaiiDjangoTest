from django.db import models

# Create your models here.


class Speaker(models.Model):
	"""This class will save spearkers"""

	firts_name = models.CharField(max_length=20)
	last_name =  models.CharField(max_length=20)
	topic = models.TextField(blank=True)
