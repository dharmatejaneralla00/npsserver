# Generated by Django 4.1.1 on 2022-09-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patent', '0004_documentationstatus_draftingstatus_drawingstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinationsatus',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ferstatus',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='hearingstatus',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
