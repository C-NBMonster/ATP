# Generated by Django 2.0.5 on 2019-03-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=10)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('depart', models.CharField(default='测试部', max_length=30)),
                ('joinTime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='已启用', max_length=10)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-joinTime'],
            },
        ),
    ]