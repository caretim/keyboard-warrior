# Generated by Django 3.2.13 on 2022-11-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_signal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='reception_user',
        ),
        migrations.RemoveField(
            model_name='room',
            name='send_user',
        ),
        migrations.RemoveField(
            model_name='room',
            name='trade',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]