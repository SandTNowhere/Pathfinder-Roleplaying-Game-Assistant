from django.db import models

class Character(models.Model):
	author = models.ForeignKey('auth.User')
	name = models.CharField(max_length=60)
	race = models.CharField(max_length=10)
	cclass = models.CharField(max_length=20)

	def publish(self):
		self.save()
	
	def __str__(self):
		return self.name
