# Generated by Django 5.0.3 on 2024-03-25 20:38

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_student_father_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_field',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='student',
            name='duration_field',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='student',
            name='email_field',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='null_boolean_field',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='time_field',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='url_field',
            field=models.URLField(default='http://google.com'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
