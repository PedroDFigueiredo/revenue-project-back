from django.db import models


# Create your models here.
class Transaction(models.Model):
	value = models.DecimalField(max_digits=6, decimal_places=2, null=False)
	description = models.CharField(max_length=500, null=True, default='?')
	is_usefull = models.BooleanField(null=False, default=True)
	date = models.DateTimeField('Datae transaction')
	last_update = models.DateTimeField('date published', auto_now=True)
	create_date = models.DateTimeField('Date criation')
