# Generated by Django 2.2.14 on 2020-09-02 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.TextField(default='none')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('tag_title', models.CharField(default='Sale', max_length=150)),
                ('tag_title_color', models.CharField(default='orange', max_length=150)),
                ('section', models.CharField(default='section_one', max_length=150)),
                ('image_1', models.ImageField(upload_to='product/images/')),
                ('image_2', models.ImageField(upload_to='product/images/')),
                ('image_3', models.ImageField(upload_to='product/images/')),
                ('image_4', models.ImageField(upload_to='product/images/')),
                ('video', models.CharField(default='jshsjssd7sjs', max_length=150)),
                ('description', models.TextField(default='none')),
                ('specification', models.TextField(default='none')),
                ('category', models.CharField(max_length=150)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('threshold', models.IntegerField(blank=True, default=1, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('old_price', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('shipping_charge', models.FloatField(blank=True, null=True)),
                ('dimension', models.CharField(max_length=150)),
                ('delivery_info', models.CharField(default='none', max_length=150)),
                ('slug', models.SlugField(default='rayslug', unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=150)),
                ('email', models.CharField(default='none', max_length=150)),
                ('review', models.TextField(default='none')),
                ('status', models.CharField(default='pending', max_length=150)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReviewConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('review', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Review')),
            ],
        ),
        migrations.CreateModel(
            name='ProductQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_shipping_charge', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Quantity')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductColorConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('color', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Color')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(through='product.ProductColorConnector', to='product.Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ManyToManyField(through='product.ProductReviewConnector', to='product.Review'),
        ),
    ]
