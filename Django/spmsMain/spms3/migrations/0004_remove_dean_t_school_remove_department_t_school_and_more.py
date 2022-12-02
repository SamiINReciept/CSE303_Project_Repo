# Generated by Django 4.1.3 on 2022-12-02 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spms3', '0003_plo_t'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dean_t',
            name='school',
        ),
        migrations.RemoveField(
            model_name='department_t',
            name='school',
        ),
        migrations.RemoveField(
            model_name='faculty_t',
            name='department',
        ),
        migrations.RemoveField(
            model_name='head_t',
            name='department',
        ),
        migrations.RemoveField(
            model_name='plo_t',
            name='program',
        ),
        migrations.RemoveField(
            model_name='program_t',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student_t',
            name='department',
        ),
        migrations.DeleteModel(
            name='Course_T',
        ),
        migrations.DeleteModel(
            name='Dean_T',
        ),
        migrations.DeleteModel(
            name='Department_T',
        ),
        migrations.DeleteModel(
            name='Faculty_T',
        ),
        migrations.DeleteModel(
            name='Head_T',
        ),
        migrations.DeleteModel(
            name='PLO_T',
        ),
        migrations.DeleteModel(
            name='Program_T',
        ),
        migrations.DeleteModel(
            name='School_T',
        ),
        migrations.DeleteModel(
            name='Student_T',
        ),
    ]