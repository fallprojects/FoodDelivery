# Generated by Django 3.1.3 on 2020-11-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineDelivery', '0002_auto_20201111_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='bowl',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coals',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hookah',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tabacco',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]