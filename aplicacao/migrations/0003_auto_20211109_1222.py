# Generated by Django 2.2.12 on 2021-11-09 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0002_auto_20211109_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoajuridica',
            old_name='TIPO_CHOICES',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='pessoafisica',
            name='TIPO_CHOICES',
        ),
    ]
