# Generated by Django 5.0.7 on 2024-10-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0003_counselingsession_session_user_alter_session_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
