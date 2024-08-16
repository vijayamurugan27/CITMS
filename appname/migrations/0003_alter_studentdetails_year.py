# Generated by Django 5.0.7 on 2024-07-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0002_studentdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='year',
            field=models.CharField(choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')], default=1, max_length=1),
        ),
    ]
