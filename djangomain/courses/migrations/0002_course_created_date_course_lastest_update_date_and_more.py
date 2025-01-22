# Generated by Django 5.1.5 on 2025-01-22 12:05

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 12, 4, 57, 717440, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='lastest_update_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 22, 12, 5, 2, 476850, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(default='student', max_length=50)),
                ('date_enroled', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
