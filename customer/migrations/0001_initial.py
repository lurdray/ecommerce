# Generated by Django 3.1.1 on 2020-09-18 09:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='none', max_length=150)),
                ('company_name', models.CharField(default='none', max_length=150)),
                ('email', models.CharField(default='none', max_length=150)),
                ('password', models.CharField(default='none', max_length=150)),
                ('country', models.CharField(default='none', max_length=150)),
                ('phone', models.CharField(default='none', max_length=150)),
                ('address', models.CharField(default='none', max_length=150)),
                ('order_note', models.CharField(default='none', max_length=150)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='WishListProductConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('wishlist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='customer.wishlist')),
            ],
        ),
        migrations.AddField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(through='customer.WishListProductConnector', to='product.Product'),
        ),
    ]
