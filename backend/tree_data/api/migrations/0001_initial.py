# Generated by Django 2.1.3 on 2018-12-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(default='NONE', max_length=1000)),
                ('display_name', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
