# Generated by Django 2.2.4 on 2020-07-19 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('total_products', models.IntegerField(blank=True, null=True)),
                ('cart_id', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CartProductQuantityConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cart', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('product_quantity', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.ProductQuantity')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product_quantitys',
            field=models.ManyToManyField(through='cart.CartProductQuantityConnector', to='product.ProductQuantity'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
