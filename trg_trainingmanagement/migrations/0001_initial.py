# Generated by Django 5.1.2 on 2024-11-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Training Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Training Description')),
                ('type', models.CharField(choices=[('onsite', 'Onsite'), ('online', 'Online'), ('hybrid', 'Hybrid')], default='onsite', max_length=50, verbose_name='Training Type')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
    ]
