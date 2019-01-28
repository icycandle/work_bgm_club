# Generated by Django 2.1.5 on 2019-01-28 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musiclink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(db_index=True, max_length=32, verbose_name='jobtype')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create_at')),
            ],
            options={
                'verbose_name': 'LinkQueue',
                'verbose_name_plural': 'LinkQueues',
            },
        ),
        migrations.CreateModel(
            name='UserQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtype', models.CharField(db_index=True, max_length=32, verbose_name='jobtype')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_queue', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserQueue',
                'verbose_name_plural': 'UserQueues',
            },
        ),
        migrations.AddField(
            model_name='musiclink',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='create_at'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='musiclink',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='linkqueue',
            name='musiclink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_queue', to='musiclink.MusicLink'),
        ),
    ]