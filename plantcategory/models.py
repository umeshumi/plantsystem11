from django.db import models

# Create your models here.
class Plant(models.Model):
	Name 	=	models.CharField(max_length=50)
	Previous_Day_Price = models.FloatField()
	Present_Day_Price = models.FloatField()
	Image 		=	models.ImageField(upload_to='catogeryImage', blank=True)
	Info 		=	models.TextField()

	def __str__(self):
		return self.Name