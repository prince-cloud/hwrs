# Generated by Django 4.0.5 on 2022-07-13 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_texttospeech_alter_translatetext_translate_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatetext',
            name='translate_to',
            field=models.CharField(blank=True, choices=[('es', 'Spanish'), ('fr', 'French'), ('de', 'German'), ('ha', 'Hausa')], max_length=100, null=True),
        ),
    ]
