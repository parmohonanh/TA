# Generated by Django 2.1.4 on 2019-01-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configure', '0010_auto_20190119_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='device',
            field=models.ManyToManyField(to='Inventory.Device'),
        ),
    ]