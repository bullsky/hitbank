# Generated by Django 2.0.3 on 2018-03-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('serial', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('s_account', models.CharField(max_length=16)),
                ('s_bankcard', models.CharField(max_length=19)),
                ('currency', models.CharField(max_length=4)),
                ('amount', models.BigIntegerField(default=0)),
                ('balance', models.BigIntegerField(default=0)),
                ('type', models.CharField(max_length=8)),
                ('target_web', models.URLField()),
                ('d_account', models.CharField(max_length=16)),
                ('d_bankcard', models.CharField(max_length=19)),
            ],
        ),
    ]