# Generated by Django 3.0.2 on 2020-03-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0013_auto_20200304_0503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postproblem',
            name='file',
        ),
        migrations.AlterField(
            model_name='postproblem',
            name='image',
            field=models.FileField(upload_to='post_pics'),
        ),
    ]
