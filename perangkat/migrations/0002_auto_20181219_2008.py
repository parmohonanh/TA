# Generated by Django 2.1.4 on 2018-12-19 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perangkat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendor',
            new_name='perangkat',
        ),
        migrations.RenameField(
            model_name='perangkat',
            old_name='seri',
            new_name='vendor',
        ),
    ]