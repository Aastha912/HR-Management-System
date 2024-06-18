# Generated by Django 5.0.1 on 2024-02-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TYApp', '0004_etable_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
