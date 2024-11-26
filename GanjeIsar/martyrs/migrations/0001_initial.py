# Generated by Django 5.1.3 on 2024-11-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Martyr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='shahidavatars')),
            ],
            options={
                'verbose_name': 'martyr',
                'verbose_name_plural': 'martyrs',
                'db_table': 'martyrs',
            },
        ),
    ]
