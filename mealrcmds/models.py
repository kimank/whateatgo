from django.db import models

# Create your models here.
class Food(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=10)
	introduction = models.TextField()
	date = models.DateTimeField()
	meal_division = models.CharField(max_length=10)
	main_ingredient = models.CharField(max_length=20)
	price = models.IntegerField(default=0)
	meal_aste = models.CharField(max_length=10)
	meal_type = models.CharField(max_length=10)