# Generated by Django 5.1.2 on 2024-11-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osha_documentationandcompliance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(choices=[('legal', 'Legal'), ('normative', 'Normative'), ('regulatory', 'Regulatory')], max_length=20),
        ),
    ]
