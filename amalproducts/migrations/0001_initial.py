# Generated by Django 2.1.4 on 2018-12-06 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('product_number', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amalproducts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('product_number',),
            },
        ),
    ]
