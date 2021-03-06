# Generated by Django 2.0.3 on 2018-03-25 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=8)),
                ('passwd', models.CharField(max_length=64)),
                ('regist_data', models.DateField()),
                ('status', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=8)),
                ('passwd', models.CharField(max_length=64)),
            ],
        ),
    ]
