# Generated by Django 4.0.5 on 2022-06-26 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_translatetext_translate_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatetext',
            name='translate_to',
            field=models.CharField(blank=True, choices=[('Spanish', 'Spanish'), ('French', 'French'), ('German', 'German')], max_length=100, null=True),
        ),
    ]
