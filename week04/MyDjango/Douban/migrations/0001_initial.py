# Generated by Django 2.2.13 on 2021-01-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_star', models.IntegerField()),
                ('short', models.CharField(max_length=400)),
                ('sentiment', models.FloatField()),
            ],
            options={
                'db_table': 't1',
                'managed': True,
            },
        ),
    ]