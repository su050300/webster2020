# Generated by Django 3.1.2 on 2020-10-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_auto_20201009_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freemovievideo',
            name='thumbnail_image',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='freeseriesvideos',
            name='thumbnail_image',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='moviedetails',
            name='thumbnail_image',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movievideo',
            name='thumbnail_image',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seriesvideos',
            name='thumbnail_image',
            field=models.IntegerField(),
        ),
    ]
