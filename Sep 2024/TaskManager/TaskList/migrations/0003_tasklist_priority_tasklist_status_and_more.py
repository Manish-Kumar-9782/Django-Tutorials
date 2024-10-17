# Generated by Django 5.1 on 2024-10-17 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskList', '0002_tasklist_created_tasklist_modified_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'high')], default='low', max_length=6),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('completed', 'Completed'), ('init', 'Init')], default='init', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'high')], default='low', max_length=15),
        ),
    ]
