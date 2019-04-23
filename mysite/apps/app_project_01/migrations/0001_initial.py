# Generated by Django 2.0.5 on 2019-03-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apprunset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(blank=True, max_length=20)),
                ('pho_name', models.CharField(blank=True, max_length=30)),
                ('serverIP', models.CharField(blank=True, max_length=20)),
                ('createby', models.CharField(blank=True, max_length=20)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('upt_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': '项目名称',
                'verbose_name_plural': 'APP运行配置',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=10)),
                ('pro_name', models.CharField(blank=True, max_length=20)),
                ('module', models.CharField(blank=True, max_length=20)),
                ('case_name1', models.CharField(blank=True, max_length=100)),
                ('case_name2', models.CharField(blank=True, max_length=100)),
                ('para1', models.CharField(blank=True, max_length=30)),
                ('para2', models.CharField(blank=True, max_length=20)),
                ('para3', models.CharField(blank=True, max_length=20)),
                ('para4', models.CharField(blank=True, max_length=20)),
                ('para5', models.CharField(blank=True, max_length=20)),
                ('para6', models.CharField(blank=True, max_length=20)),
                ('para7', models.CharField(blank=True, max_length=20)),
                ('para8', models.CharField(blank=True, max_length=20)),
                ('para9', models.CharField(blank=True, max_length=20)),
                ('para10', models.CharField(blank=True, max_length=20)),
                ('para11', models.CharField(blank=True, max_length=20)),
                ('para12', models.CharField(blank=True, max_length=20)),
                ('createby', models.CharField(blank=True, max_length=20)),
                ('updateby', models.CharField(blank=True, max_length=20)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('upt_time', models.DateTimeField(auto_now_add=True)),
                ('run', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': '项目名称',
                'verbose_name_plural': '用例库',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(blank=True, max_length=100)),
                ('r_type', models.CharField(blank=True, choices=[('get', 'get'), ('post', 'post')], default='get', max_length=10)),
                ('result', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name': '用例名称',
                'verbose_name_plural': '接口测试',
            },
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(blank=True, max_length=100)),
                ('module', models.CharField(blank=True, max_length=20)),
                ('case_name', models.CharField(blank=True, max_length=100)),
                ('case_total', models.CharField(blank=True, max_length=10)),
                ('case_pass', models.CharField(blank=True, max_length=10)),
                ('case_fail', models.CharField(blank=True, max_length=10)),
                ('case_jump', models.CharField(blank=True, max_length=10)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('s_time', models.DateTimeField(auto_now_add=True)),
                ('e_time', models.DateTimeField(auto_now_add=True)),
                ('reson', models.CharField(blank=True, max_length=1000)),
                ('result', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name': '项目名称',
                'verbose_name_plural': '测试报告',
                'ordering': ['-s_time'],
            },
        ),
        migrations.CreateModel(
            name='runHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(blank=True, max_length=20)),
                ('pho_name', models.CharField(blank=True, max_length=30)),
                ('serverIP', models.CharField(blank=True, max_length=20)),
                ('excuteby', models.CharField(blank=True, max_length=20)),
                ('caseTotle', models.CharField(blank=True, max_length=5)),
                ('casePass', models.CharField(blank=True, max_length=5)),
                ('caseFail', models.CharField(blank=True, max_length=5)),
                ('caseJump', models.CharField(blank=True, max_length=5)),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('endTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '项目名称',
                'verbose_name_plural': '运行历史',
                'ordering': ['-startTime'],
            },
        ),
        migrations.CreateModel(
            name='webrunset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, default=None)),
                ('pro_name', models.CharField(blank=True, max_length=20)),
                ('browser_name', models.CharField(blank=True, max_length=30)),
                ('serverIP', models.CharField(blank=True, max_length=20)),
                ('createby', models.CharField(blank=True, max_length=20)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('upt_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': '项目名称',
                'verbose_name_plural': 'Web运行配置',
                'ordering': ['-c_time'],
            },
        ),
    ]