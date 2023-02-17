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

class Category(models.Model):
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'media/slider', blank = True)

class Products(models.Model):
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

class FAQ(models.Model):
	question_uz = models.CharField(max_length = 1000, blank = True)
	question_ru = models.CharField(max_length = 1000, blank = True)
	question_en = models.CharField(max_length = 1000, blank = True)
	answer_uz = models.CharField(max_length = 10000, blank = True)
	answer_ru = models.CharField(max_length = 10000, blank = True)
	answer_en = models.CharField(max_length = 10000, blank = True)