# Generated by Django 4.2.16 on 2024-11-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0003_alter_attendancetable_attendance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logintable',
            name='status',
            field=models.CharField(blank=True, default='Reject', max_length=50, null=True),
        ),
    ]
