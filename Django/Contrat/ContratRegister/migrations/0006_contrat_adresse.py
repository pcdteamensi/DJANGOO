# Generated by Django 2.1.7 on 2019-03-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContratRegister', '0005_contrat_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='adresse',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
