# Generated by Django 4.2.9 on 2024-03-10 10:33

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='added',
            field=myapp.models.CustomDateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='intensity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='likelihood',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='relevance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
