# Generated by Django 3.1.2 on 2020-11-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Segment', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Product', models.CharField(max_length=100)),
                ('Units', models.IntegerField()),
                ('Sales', models.IntegerField()),
                ('Datesold', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ProductModel',
                'verbose_name_plural': 'ProductModels',
            },
        ),
    ]
