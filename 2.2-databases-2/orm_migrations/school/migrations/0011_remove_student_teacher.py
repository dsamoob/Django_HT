# Generated by Django 4.1.2 on 2022-11-01 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
