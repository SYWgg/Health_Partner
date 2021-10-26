# Generated by Django 3.2.7 on 2021-10-25 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_remove_board_updated_at'),
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='boardapp.board'),
        ),
    ]
