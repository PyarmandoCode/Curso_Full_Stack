# Generated by Django 3.2.17 on 2023-02-07 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_post_subtitulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tapa',
            new_name='imagen',
        ),
    ]
