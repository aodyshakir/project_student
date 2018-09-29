# Generated by Django 2.1.1 on 2018-09-23 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellingportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_degree', models.IntegerField(default=15)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellingportal.Student')),
            ],
        ),
    ]