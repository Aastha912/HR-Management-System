# Generated by Django 5.0.1 on 2024-03-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TYApp', '0007_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcementtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='announcement_images/')),
                ('position', models.CharField(max_length=100)),
                ('qualification_experience', models.TextField()),
                ('job_description', models.TextField()),
                ('event_date', models.DateField()),
                ('expected_salary', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('full_time', 'Full Time'), ('fresher', 'Fresher'), ('internship', 'Internship'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('temporary', 'Temporary')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
    ]
