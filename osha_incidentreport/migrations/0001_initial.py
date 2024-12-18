# Generated by Django 5.1.2 on 2024-11-18 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('identification_number', models.CharField(max_length=20)),
                ('identification_document', models.CharField(max_length=100)),
                ('type_accident', models.CharField(choices=[('typical', 'Typical'), ('atypical', 'Atypical'), ('path', 'Path'), ('occupational', 'Occupational')], default='atypical', max_length=20)),
                ('accident_location', models.CharField(max_length=100)),
                ('type_injury', models.CharField(max_length=100)),
                ('time_away', models.IntegerField()),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_crm', models.CharField(max_length=10)),
            ],
        ),
    ]
