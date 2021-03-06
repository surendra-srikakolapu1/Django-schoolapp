# Generated by Django 3.1.7 on 2021-07-01 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('fathername', models.CharField(max_length=1000)),
                ('classname', models.IntegerField()),
                ('contact', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('age', models.PositiveIntegerField()),
                ('subject', models.CharField(choices=[('Mathematics', 'Mathematics'), ('Telugu', 'Telugu'), ('English', 'English'), ('Hindi', 'Hindi'), ('Science', 'Science'), ('Social', 'Social')], max_length=15)),
                ('email', models.EmailField(max_length=40)),
                ('contact', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fee', models.CharField(max_length=30, null=True)),
                ('fees_paid', models.CharField(max_length=30, null=True)),
                ('fees_due', models.CharField(max_length=30, null=True)),
                ('paid_date', models.DateField(null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admissions.student')),
            ],
        ),
    ]
