# Generated by Django 3.1.2 on 2020-10-20 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('provider', '0009_videorejectioncomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.videos')),
            ],
            options={
                'verbose_name_plural': 'Video Comment',
            },
        ),
        migrations.CreateModel(
            name='SeriesRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('series_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.seriesdetails')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Series Rating',
            },
        ),
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.moviedetails')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Movie Rating',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_watched', models.PositiveSmallIntegerField()),
                ('timestamp', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.videos')),
            ],
            options={
                'verbose_name_plural': 'History',
            },
        ),
    ]