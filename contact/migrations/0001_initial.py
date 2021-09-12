# Generated by Django 3.2.3 on 2021-09-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('pickup_location', models.CharField(blank=True, max_length=300)),
                ('start_time', models.TimeField(auto_now_add=True, null=True)),
                ('end_time', models.TimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]