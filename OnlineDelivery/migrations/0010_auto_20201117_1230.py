# Generated by Django 3.1.3 on 2020-11-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineDelivery', '0009_sales_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complect',
            name='price',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='price',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
