# Generated by Django 4.1.2 on 2022-11-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_student_teacher_delete_studentteachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='Учитель', to='school.teacher'),
        ),
    ]
