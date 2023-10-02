# Generated by Django 4.2.5 on 2023-10-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]