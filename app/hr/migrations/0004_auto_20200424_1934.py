# Generated by Django 3.0.5 on 2020-04-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20200424_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='orderDate',
            field=models.DateField(auto_now=True),
        ),
    ]