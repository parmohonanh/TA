# Generated by Django 2.1.4 on 2019-01-18 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Configure', '0003_auto_20190118_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='command',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Configure.Command'),
        ),
    ]
