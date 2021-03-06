# Generated by Django 2.1.7 on 2019-03-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('adresse', models.EmailField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contrat_Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrat_test', models.CharField(max_length=200)),
            ],
        ),
    ]
