# Generated by Django 4.2.16 on 2024-12-13 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0021_rename_teacher_classtable_teachername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetabletable',
            old_name='StarTime',
            new_name='StartTime',
        ),
        migrations.RenameField(
            model_name='timetabletable',
            old_name='Subject',
            new_name='SubjectName',
        ),
        migrations.RenameField(
            model_name='timetabletable',
            old_name='Teacher',
            new_name='TeacherName',
        ),
    ]