# Generated by Django 5.0.6 on 2024-06-06 04:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_type', models.CharField(choices=[('Accident', 'Accident'), ('Water Leakage', 'Water Leakage'), ('Pothole', 'Pothole'), ('Borehole', 'Borehole'), ('Broken Facility', 'Broken Facility')], max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='complaints/')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
