# Generated by Django 2.1.7 on 2019-02-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('Project_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Project_Descrip', models.CharField(max_length=500)),
                ('Project_year', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('Skill_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Skill_Descrip', models.CharField(max_length=500)),
                ('Skill_rank', models.IntegerField(null=True)),
            ],
        ),
    ]
