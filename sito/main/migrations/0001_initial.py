# Generated by Django 2.2.12 on 2021-04-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_immagine', models.ImageField(blank=True, null=True, upload_to='')),
                ('ruolo', models.CharField(max_length=100, null=True)),
                ('posizione', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]