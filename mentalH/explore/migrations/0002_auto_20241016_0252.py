from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='type',
            field=models.CharField(default='regular', max_length=50),
        ),
    ]