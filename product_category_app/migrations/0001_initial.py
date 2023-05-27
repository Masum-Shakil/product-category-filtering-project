# Generated by Django 4.2.1 on 2023-05-26 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Warranties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty_year', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.FloatField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_brands', to='product_category_app.brands')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_sellers', to='product_category_app.sellers')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_type', to='product_category_app.producttypes')),
                ('warranty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products_warranty', to='product_category_app.warranties')),
            ],
        ),
    ]
