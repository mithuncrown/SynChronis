# Generated by Django 4.2.16 on 2024-12-13 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0019_rename_guardian_phone_number_studenttable_guardian_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaveapplicationtable',
            old_name='STUDENT',
            new_name='StudentName',
        ),
        migrations.RenameField(
            model_name='notestable',
            old_name='Subject_name',
            new_name='SubjectName',
        ),
        migrations.RenameField(
            model_name='studentnoticetable',
            old_name='Notice',
            new_name='Notice_Content',
        ),
        migrations.RenameField(
            model_name='studentnoticetable',
            old_name='Student',
            new_name='StudentName',
        ),
        migrations.RenameField(
            model_name='subjecttable',
            old_name='Subject_name',
            new_name='SubjectName',
        ),
        migrations.RenameField(
            model_name='teachernoticetable',
            old_name='Teacher',
            new_name='TeacherName',
        ),
    ]
