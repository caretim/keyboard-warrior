# Generated by Django 3.2.13 on 2022-11-10 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_remove_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reviews.reviews'),
            preserve_default=False,
        ),
    ]
