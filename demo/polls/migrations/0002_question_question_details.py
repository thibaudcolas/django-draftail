# Generated by Django 2.2.4 on 2019-08-19 23:03

import draftail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("polls", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="question",
            name="question_details",
            field=draftail.fields.RichTextField(
                blank=True, default=None, null=True
            ),
        )
    ]
