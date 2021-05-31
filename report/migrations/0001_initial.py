# Generated by Django 3.2 on 2021-05-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('petroleum_product', models.CharField(max_length=264)),
                ('sale', models.IntegerField()),
                ('country', models.CharField(max_length=264)),
            ],
        ),
    ]
