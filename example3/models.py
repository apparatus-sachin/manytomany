from django.db import models

class language(models.Model):
	name = models.CharField(max_length=100)

class app(models.Model):
	name = models.CharField(max_length=100)
	language = models.ForeignKey(language,on_delete=models.CASCADE)
