# Generated by Django 3.2.13 on 2022-11-17 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('reception_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='받는사람', to=settings.AUTH_USER_MODEL)),
                ('send_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.trades')),
            ],
        ),
    ]