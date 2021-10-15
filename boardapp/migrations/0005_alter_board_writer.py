# Generated by Django 3.2.7 on 2021-10-14 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boardapp', '0004_auto_20211015_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
