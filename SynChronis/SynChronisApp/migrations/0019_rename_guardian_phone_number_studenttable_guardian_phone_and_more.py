# Generated by Django 4.2.16 on 2024-12-13 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0018_timetabletable_endtime_timetabletable_startime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenttable',
            old_name='Guardian_phone_number',
            new_name='Guardian_phone',
        ),
        migrations.RenameField(
            model_name='studenttable',
            old_name='Name',
            new_name='Semester',
        ),
        migrations.RenameField(
            model_name='teachertable',
            old_name='Name',
            new_name='TeacherName',
        ),
        migrations.RemoveField(
            model_name='attendancetable',
            name='STUDENT',
        ),
        migrations.AddField(
            model_name='attendancetable',
            name='StudentName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.studenttable'),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='Class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.classtable'),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='StudentName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='classtable',
            name='TEACHER',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.teachertable'),
        ),
        migrations.AlterField(
            model_name='leaveapplicationtable',
            name='STUDENT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.studenttable'),
        ),
        migrations.AlterField(
            model_name='notestable',
            name='Class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.classtable'),
        ),
        migrations.AlterField(
            model_name='notestable',
            name='Subject_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.subjecttable'),
        ),
        migrations.AlterField(
            model_name='notestable',
            name='Teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.teachertable'),
        ),
        migrations.AlterField(
            model_name='studentnoticetable',
            name='Student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.studenttable'),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='LOGIN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.logintable'),
        ),
        migrations.AlterField(
            model_name='subjecttable',
            name='Class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.classtable'),
        ),
        migrations.AlterField(
            model_name='subjecttable',
            name='Teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.teachertable'),
        ),
        migrations.AlterField(
            model_name='teachernoticetable',
            name='Teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.teachertable'),
        ),
        migrations.AlterField(
            model_name='teachertable',
            name='LOGIN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.logintable'),
        ),
        migrations.AlterField(
            model_name='timetabletable',
            name='Class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.classtable'),
        ),
        migrations.AlterField(
            model_name='timetabletable',
            name='Teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SynChronisApp.teachertable'),
        ),
    ]