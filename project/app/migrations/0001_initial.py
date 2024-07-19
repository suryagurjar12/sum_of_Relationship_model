# Generated by Django 5.0.7 on 2024-07-19 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_name', models.CharField(max_length=50)),
                ('Stu_email', models.EmailField(max_length=254)),
                ('Stu_add', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scl_name', models.CharField(max_length=50)),
                ('C_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('Stu_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('T_name', models.ManyToManyField(to='app.teacher')),
            ],
        ),
    ]
