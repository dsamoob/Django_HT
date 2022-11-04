# Generated by Django 4.1.2 on 2022-11-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_studentteachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teachers', to='school.teacher'),
        ),
        migrations.DeleteModel(
            name='StudentTeachers',
        ),
    ]
