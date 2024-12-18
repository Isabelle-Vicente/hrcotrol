# Generated by Django 5.1.2 on 2024-11-17 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recrut_applicant', '0001_initial'),
        ('recrut_vacancymanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantScreening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_skills', models.IntegerField(default=0)),
                ('score_experience', models.IntegerField(default=0)),
                ('score_compatibility', models.IntegerField(default=0)),
                ('comments', models.TextField(blank=True, null=True)),
                ('screening_date', models.DateField(auto_now_add=True)),
                ('reviewer', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenings', to='recrut_applicant.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenings', to='recrut_vacancymanagement.jobdetails')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantTesting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_score', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testings', to='recrut_applicant.applicant')),
                ('screening', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recrut_screening.applicantscreening')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantInterviewing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_score', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('scheduled_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='recrut_applicant.applicant')),
                ('testing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recrut_screening.applicanttesting')),
            ],
        ),
    ]
