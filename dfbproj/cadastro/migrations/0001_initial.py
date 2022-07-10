# Generated by Django 4.0.5 on 2022-07-09 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'linguagens',
            },
        ),
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('salario', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='programadores', to='cadastro.empresa')),
                ('linguagens', models.ManyToManyField(related_name='programadores', to='cadastro.linguagem')),
            ],
            options={
                'verbose_name_plural': 'programadores',
            },
        ),
    ]
