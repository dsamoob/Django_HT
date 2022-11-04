# Generated by Django 4.1.2 on 2022-11-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_remove_student_teacher_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teachers', to='school.teacher'),
        ),
    ]