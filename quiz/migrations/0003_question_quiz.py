# Generated by Django 3.1 on 2020-08-07 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200807_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz'),
        ),
    ]
