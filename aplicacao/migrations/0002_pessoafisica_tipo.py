# Generated by Django 3.2.9 on 2021-11-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoafisica',
            name='tipo',
            field=models.CharField(choices=[('C', 'Comercial'), ('F', 'Fixo'), ('P', 'Pessoal')], default='P', max_length=1, verbose_name='Tip Fone:'),
        ),
    ]
