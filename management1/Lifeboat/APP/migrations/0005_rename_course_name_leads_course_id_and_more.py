# Generated by Django 5.0.6 on 2024-07-02 09:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_rename_course_name_students_course_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leads',
            old_name='course_name',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='trainers',
            old_name='course_name',
            new_name='course_id',
        ),
        migrations.AddField(
            model_name='batches',
            name='leads',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainers',
            name='trainer_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
