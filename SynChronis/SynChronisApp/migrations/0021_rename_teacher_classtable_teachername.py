# Generated by Django 4.2.16 on 2024-12-13 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0020_rename_student_leaveapplicationtable_studentname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classtable',
            old_name='TEACHER',
            new_name='TeacherName',
        ),
    ]
