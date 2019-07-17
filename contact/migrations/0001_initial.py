# Generated by Django 2.1.3 on 2019-06-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=64)),
                ('budget', models.SmallIntegerField()),
                ('phone', models.BigIntegerField()),
                ('requirements', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]