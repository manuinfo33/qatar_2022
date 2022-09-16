# Generated by Django 4.0.6 on 2022-08-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('document', models.IntegerField(max_length=8)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]