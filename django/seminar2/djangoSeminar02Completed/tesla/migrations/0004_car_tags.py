# Generated by Django 4.1.1 on 2022-10-03 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesla', '0003_remove_car_tags_tagtocar'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='tags',
            field=models.ManyToManyField(through='tesla.TagToCar', to='tesla.tag'),
        ),
    ]