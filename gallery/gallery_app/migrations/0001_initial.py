# Generated by Django 3.0.2 on 2020-12-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_category', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
