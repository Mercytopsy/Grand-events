# Generated by Django 2.0 on 2018-08-02 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionmodel',
            name='flwRef',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
