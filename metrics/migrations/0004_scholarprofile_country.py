# Generated by Django 2.2.3 on 2019-07-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0003_auto_20190715_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarprofile',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
