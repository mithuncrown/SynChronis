# Generated by Django 4.2.16 on 2024-11-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0008_rename_attendance_attendancetable_attendance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationtable',
            name='TEACHER',
        ),
        migrations.AddField(
            model_name='classtable',
            name='Location_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='classtable',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='classtable',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
