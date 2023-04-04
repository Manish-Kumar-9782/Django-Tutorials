# Generated by Django 4.1.7 on 2023-04-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=30)),
                ('Std', models.CharField(default='', max_length=10)),
                ('RollNo', models.CharField(default='', max_length=10)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=50)),
                ('Address', models.CharField(max_length=100)),
                ('Stream', models.CharField(max_length=5)),
            ],
        ),
    ]
