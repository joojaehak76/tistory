# Generated by Django 4.1.3 on 2022-11-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Not to disclose')], default=0),
            preserve_default=False,
        ),
    ]
