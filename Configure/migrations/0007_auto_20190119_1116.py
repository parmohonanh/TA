# Generated by Django 2.1.4 on 2019-01-19 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configure', '0006_auto_20190118_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automation',
            name='command',
        ),
        migrations.AddField(
            model_name='automation',
            name='command',
            field=models.ManyToManyField(to='Configure.Command'),
        ),
    ]