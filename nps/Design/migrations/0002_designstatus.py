# Generated by Django 4.1.1 on 2022-09-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Design', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20)),
                ('quotationstatus', models.CharField(max_length=20)),
                ('quotedamount', models.CharField(max_length=20)),
                ('toassignteam', models.CharField(max_length=20)),
                ('projectduedate', models.CharField(max_length=20)),
                ('designcompleted', models.BooleanField(max_length=20)),
            ],
        ),
    ]
