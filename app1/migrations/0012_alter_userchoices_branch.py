# Generated by Django 3.2.23 on 2024-02-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_userchoices_userphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchoices',
            name='branch',
            field=models.CharField(choices=[('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Electronics', 'Electronics'), ('Civil Engineering', 'Civil Engineering'), ('Economics', 'Economics'), ('Computer Science', 'Computer Science'), ('Electrical Engineering', 'Electrical Engineering'), ('Eph', 'Eph'), ('Mathematics and Computing', 'Mathematics and Computing'), ('GPT', 'GPT'), ('GT', 'GT'), ('Metallurgy', 'Metallurgy'), ('Biotech', 'Biotech'), ('Chemical Science', 'Chemical Science'), ('DSAI', 'DSAI'), ('PnI', 'PnI'), ('Architecture', 'Architecture')], max_length=100),
        ),
    ]
