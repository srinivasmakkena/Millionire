# Generated by Django 4.1.7 on 2023-05-28 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Max_Award', models.IntegerField(blank=True, null=True)),
                ('Max_questions', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
