# Generated by Django 4.1.7 on 2023-02-17 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=1000)),
                ('name_ru', models.CharField(blank=True, max_length=1000)),
                ('name_en', models.CharField(blank=True, max_length=1000)),
                ('description_uz', models.CharField(blank=True, max_length=10000)),
                ('description_ru', models.CharField(blank=True, max_length=10000)),
                ('description_en', models.CharField(blank=True, max_length=10000)),
                ('image', models.ImageField(blank=True, upload_to='images/slider')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uz', models.CharField(blank=True, max_length=1000)),
                ('question_ru', models.CharField(blank=True, max_length=1000)),
                ('question_en', models.CharField(blank=True, max_length=1000)),
                ('answer_uz', models.CharField(blank=True, max_length=10000)),
                ('answer_ru', models.CharField(blank=True, max_length=10000)),
                ('answer_en', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=1000)),
                ('name_ru', models.CharField(blank=True, max_length=1000)),
                ('name_en', models.CharField(blank=True, max_length=1000)),
                ('description_uz', models.CharField(blank=True, max_length=10000)),
                ('description_ru', models.CharField(blank=True, max_length=10000)),
                ('description_en', models.CharField(blank=True, max_length=10000)),
                ('image', models.ImageField(blank=True, upload_to='images/slider')),
                ('link', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(blank=True, max_length=100)),
                ('name_uz', models.CharField(blank=True, max_length=1000)),
                ('name_ru', models.CharField(blank=True, max_length=1000)),
                ('name_en', models.CharField(blank=True, max_length=1000)),
                ('description_uz', models.CharField(blank=True, max_length=10000)),
                ('description_ru', models.CharField(blank=True, max_length=10000)),
                ('description_en', models.CharField(blank=True, max_length=10000)),
                ('image', models.ImageField(blank=True, upload_to='images/slider')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
            ],
        ),
    ]