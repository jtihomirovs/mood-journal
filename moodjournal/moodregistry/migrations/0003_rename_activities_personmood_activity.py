# Generated by Django 4.0.3 on 2022-03-29 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moodregistry', '0002_personmood_created_at_personmood_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personmood',
            old_name='activities',
            new_name='activity',
        ),
    ]
