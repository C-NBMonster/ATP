# Generated by Django 2.0.5 on 2019-03-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='td',
            name='p7',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='td',
            name='p1',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='td',
            name='p5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='td',
            name='p6',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
