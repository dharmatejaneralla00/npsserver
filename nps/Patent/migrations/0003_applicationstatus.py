# Generated by Django 4.0.4 on 2022-09-08 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patent', '0002_alter_patentapplication_modeofcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
                ('paymentstatus', models.BooleanField(default=False)),
            ],
        ),
    ]
