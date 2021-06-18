# Generated by Django 3.2.4 on 2021-06-17 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_file', models.CharField(max_length=100)),
                ('doc_num', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('patronymic', models.CharField(max_length=100)),
                ('birth_date', models.DateField(max_length=100)),
                ('personal_number', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('issue_date', models.DateField(max_length=200)),
                ('expire_date', models.DateField(max_length=200)),
                ('issuing_authority', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='customers.customer')),
            ],
        ),
    ]
