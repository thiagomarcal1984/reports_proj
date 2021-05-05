# Generated by Django 3.1.7 on 2021-05-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20210421_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='activated',
        ),
        migrations.AddField(
            model_name='csv',
            name='csv_file',
            field=models.FileField(null=True, upload_to='csvs'),
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
