# Generated by Django 4.2.13 on 2024-07-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlForDataAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csv_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
