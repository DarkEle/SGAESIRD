from django.db import models

# Create your models here.

class Domain(models.Model):
	id_domain = models.AutoField(primary_key=True, help_text="ID")
	name = models.CharField(default = "No information available", max_length=200)
	def __str__(self):
		return self.name
