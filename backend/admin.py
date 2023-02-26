from django.contrib import admin
from .models import *

class SliderAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_uz')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_uz')

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name_uz')

class FAQAdmin(admin.ModelAdmin):
	list_display = ('id', 'question_uz')

admin.site.register(Slider, SliderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(FAQ, FAQAdmin)