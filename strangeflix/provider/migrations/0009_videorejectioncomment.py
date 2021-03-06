# Generated by Django 3.1.2 on 2020-10-13 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0008_auto_20201009_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoRejectionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.videos')),
            ],
            options={
                'verbose_name_plural': 'Video Rejection Comment',
            },
        ),
    ]
