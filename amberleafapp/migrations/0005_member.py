# Generated by Django 5.1.3 on 2024-12-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amberleafapp', '0004_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
