# Generated by Django 4.2.16 on 2024-11-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SynChronisApp', '0005_alter_logintable_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]