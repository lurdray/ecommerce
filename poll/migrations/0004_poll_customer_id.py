# Generated by Django 3.1.1 on 2020-09-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20200923_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='customer_id',
            field=models.CharField(default='none', max_length=1050),
        ),
    ]
