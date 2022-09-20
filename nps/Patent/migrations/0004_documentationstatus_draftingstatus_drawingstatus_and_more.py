# Generated by Django 4.1.1 on 2022-09-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patent', '0003_applicationstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DraftingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DrawingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ExaminationSatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FilingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GrantsStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HearingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NDAStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
                ('nda', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NoveltyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=20)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ApplicationStatus',
        ),
    ]
