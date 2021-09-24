# Generated by Django 3.2.7 on 2021-09-23 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_section'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['posizione']},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='posizione',
        ),
        migrations.AddField(
            model_name='section',
            name='foto1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.photo'),
        ),
        migrations.AddField(
            model_name='section',
            name='posizione',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
