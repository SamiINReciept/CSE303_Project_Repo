# Generated by Django 4.1.3 on 2022-12-02 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spms3', '0006_remove_course_evaluation_t_courseid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='COURSE_OUTLINE_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseTitle', models.CharField(max_length=50)),
                ('CourseType', models.CharField(max_length=50)),
                ('CreditValue', models.CharField(max_length=50)),
                ('ContactHourOrWeek', models.CharField(max_length=50)),
                ('CourseDescription', models.CharField(max_length=2000)),
                ('CourseObjective', models.CharField(max_length=2000)),
                ('CourseContent', models.CharField(max_length=2000)),
                ('AssessmentType', models.CharField(max_length=50)),
                ('ReferenceBook', models.CharField(max_length=500)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spms3.course_t')),
            ],
        ),
        migrations.CreateModel(
            name='COURSE_LESSON_T',
            fields=[
                ('Week', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Topic', models.CharField(max_length=500)),
                ('TeachingStrategy', models.CharField(max_length=500)),
                ('AssessmentStrategy', models.CharField(max_length=500, null=True)),
                ('CLOLevel', models.CharField(max_length=50)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spms3.course_outline_t')),
            ],
        ),
        migrations.CreateModel(
            name='COURSE_EVALUATION_T',
            fields=[
                ('AssessmentTools', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('MarksDist', models.CharField(max_length=50)),
                ('BloomCategory', models.CharField(max_length=500)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spms3.course_outline_t')),
            ],
        ),
    ]