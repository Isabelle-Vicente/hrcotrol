# Generated by Django 5.1.2 on 2024-11-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_rename_cpf_employee_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images/'),
        ),
    ]