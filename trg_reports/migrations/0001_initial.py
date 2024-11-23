# Generated by Django 5.1.2 on 2024-11-23 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trg_trainingmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Report Title')),
                ('report_type', models.CharField(choices=[('attendance', 'Attendance'), ('performance', 'Performance'), ('feedback', 'Feedback'), ('general', 'General Overview')], default='general', max_length=50, verbose_name='Report Type')),
                ('generated_at', models.DateTimeField(auto_now_add=True, verbose_name='Generated At')),
                ('data', models.JSONField(verbose_name='Report Data')),
                ('created_by', models.CharField(max_length=100, verbose_name='Generated By')),
                ('training', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='trg_trainingmanagement.training', verbose_name='Related Training')),
            ],
        ),
    ]
