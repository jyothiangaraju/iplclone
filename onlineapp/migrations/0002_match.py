# Generated by Django 2.2.1 on 2019-06-17 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inning', models.IntegerField()),
                ('batting_team', models.CharField(max_length=128)),
                ('bowling_team', models.CharField(max_length=128)),
                ('over', models.IntegerField()),
                ('ball', models.IntegerField()),
                ('batsman', models.CharField(max_length=128)),
                ('non_striker', models.CharField(max_length=128)),
                ('bowler', models.CharField(max_length=128)),
                ('is_super_over', models.BooleanField()),
                ('wide_runs', models.IntegerField()),
                ('bye_runs', models.IntegerField()),
                ('legbye_runs', models.IntegerField()),
                ('noball_runs', models.IntegerField()),
                ('penalty_runs', models.IntegerField()),
                ('batsman_runs', models.IntegerField()),
                ('extra_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
                ('player_dismissed', models.CharField(max_length=128)),
                ('dismissal_kind', models.CharField(max_length=128)),
                ('fielder', models.CharField(max_length=128)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.Season')),
            ],
        ),
    ]
