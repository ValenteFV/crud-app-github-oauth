# Generated by Django 3.0.4 on 2020-03-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_profile', '0002_auto_20200316_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('unspecified', 'Unspecified'), ('other', 'Other / I rather not say')], max_length=200, null=True),
        ),
    ]
