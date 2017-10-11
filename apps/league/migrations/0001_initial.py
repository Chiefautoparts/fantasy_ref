# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ref_home', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('league_admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
                ('team_location', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='login.User')),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='ref_home.Ref')),
            ],
        ),
        migrations.AddField(
            model_name='league',
            name='members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='league.Team'),
        ),
    ]