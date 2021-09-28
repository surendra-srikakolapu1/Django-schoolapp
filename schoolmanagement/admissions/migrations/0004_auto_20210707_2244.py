# Generated by Django 3.1.7 on 2021-07-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_auto_20210701_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classname',
            field=models.CharField(choices=[('Nursery', 'Nursery'), ('L.K.G', 'L.K.G'), ('U.K.G', 'U.K.G'), ('1ˢᵗ', '1ˢᵗ'), ('2ⁿᵈ', '2ⁿᵈ'), ('3ʳᵈ', '3ʳᵈ'), ('4ᵗʰ', '4ᵗʰ'), ('5ᵗʰ', '5ᵗʰ'), ('6ᵗʰ', '6ᵗʰ'), ('7ᵗʰ', '7ᵗʰ'), ('8ᵗʰ', '8ᵗʰ'), ('9ᵗʰ', '9ᵗʰ'), ('10ᵗʰ', '10ᵗʰ')], max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=400),
        ),
    ]