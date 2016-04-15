# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('is_valid', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Gm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('long', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('bonus', models.IntegerField()),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.IntegerField()),
                ('question', models.CharField(max_length=400)),
                ('answers', models.ManyToManyField(to='main.Answer')),
            ],
        ),
        migrations.AddField(
            model_name='quest',
            name='questions',
            field=models.ManyToManyField(to='main.Question'),
        ),
        migrations.AddField(
            model_name='gm',
            name='locations',
            field=models.ManyToManyField(to='main.Location'),
        ),
        migrations.AddField(
            model_name='gm',
            name='quests',
            field=models.ManyToManyField(to='main.Quest'),
        ),
    ]
