# Generated by Django 4.2.7 on 2023-11-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('link', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='resources')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Developer', 'User'), ('staff', 'Staff')], max_length=10),
        ),
    ]
