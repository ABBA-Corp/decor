from django.db import models

class Slider(models.Model):
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'media/slider', blank = True)
	link = models.CharField(max_length = 1000, blank = True)

	def __str__(self):
		return self.name_uz

class Category(models.Model):
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'media/slider', blank = True)

	def __str__(self):
		return self.name_uz

class Product(models.Model):
	category_id = models.ForeignKey('Category', on_delete = models.CASCADE, blank = True)
	price = models.CharField(max_length = 100, blank = True)
	size = models.CharField(max_length = 100, blank = True)
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'media/slider', blank = True)
	image1 = models.ImageField(upload_to = 'media/slider', blank = True)

	def __str__(self):
		return self.name_uz

class FAQ(models.Model):
	question_uz = models.CharField(max_length = 1000, blank = True)
	question_ru = models.CharField(max_length = 1000, blank = True)
	question_en = models.CharField(max_length = 1000, blank = True)
	answer_uz = models.CharField(max_length = 10000, blank = True)
	answer_ru = models.CharField(max_length = 10000, blank = True)
	answer_en = models.CharField(max_length = 10000, blank = True)

	def __str__(self):
		return self.question_uz