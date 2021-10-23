from django.db import models

class Todolist(models.Model):
	title = models.CharField(max_length=100)
	detail = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title