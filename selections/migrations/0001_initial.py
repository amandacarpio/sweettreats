# Generated by Django 4.1.7 on 2023-02-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Selections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dessert_Name', models.CharField(max_length=50)),
                ('Allergies', models.BooleanField()),
                ('If_yes_please_specify', models.CharField(max_length=100, null=True)),
                ('Dessert_Details', models.CharField(max_length=500)),
                ('Email', models.CharField(max_length=50)),
                ('Budget', models.CharField(choices=[('Low', '$1-$50'), ('Medium', '$51-$100'), ('High', '$101+')], default='Low', max_length=6)),
            ],
        ),
    ]
