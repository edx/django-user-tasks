# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 15:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTaskArtifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(default='Output', help_text='Distinguishes between multiple artifact types for the same task', max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('url', models.URLField(blank=True)),
                ('text', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('task_id', models.CharField(db_index=True, help_text='UUID of the associated Celery task', max_length=128, unique=True)),
                ('is_container', models.BooleanField(default=False, help_text='True if this status corresponds to a container of multiple tasks')),
                ('task_class', models.CharField(help_text='Fully qualified class name of the task being performed', max_length=128)),
                ('name', models.CharField(help_text='A name for this task which the triggering user will understand', max_length=255)),
                ('state', models.CharField(default='Pending', max_length=128)),
                ('completed_steps', models.PositiveSmallIntegerField(default=0)),
                ('total_steps', models.PositiveSmallIntegerField()),
                ('attempts', models.PositiveSmallIntegerField(default=1, help_text='How many times has execution been attempted?')),
                ('parent', models.ForeignKey(blank=True, default=None, help_text='Status of the containing task grouping (if any)', null=True, on_delete=django.db.models.deletion.CASCADE, to='user_tasks.UserTaskStatus')),
                ('user', models.ForeignKey(help_text='The user who triggered the task', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='usertaskartifact',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_tasks.UserTaskStatus'),
        ),
    ]
