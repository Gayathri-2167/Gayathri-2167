# Generated by Django 5.0.6 on 2024-07-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_rename_paymets_payments_alter_students_batche_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='course_name',
            new_name='course_id',
        ),
        migrations.AddField(
            model_name='courses',
            name='course_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
