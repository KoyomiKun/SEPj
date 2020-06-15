# Generated by Django 3.0.7 on 2020-06-07 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('admin_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('admin_email', models.CharField(blank=True, max_length=32, null=True)),
                ('admin_record', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'admins',
            },
        ),
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('record_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('record_time', models.DateField(blank=True, null=True)),
                ('record_start', models.CharField(blank=True, max_length=30, null=True)),
                ('record_end', models.CharField(blank=True, max_length=30, null=True)),
                ('record_condition', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_record',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=16)),
                ('user_email', models.CharField(blank=True, max_length=32, null=True)),
                ('user_phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'users_',
            },
        ),
        migrations.CreateModel(
            name='SubmitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id1', models.ForeignKey(blank=True, db_column='record_id1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='API.UserRecord')),
                ('user_id2', models.ForeignKey(blank=True, db_column='user_id2', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='API.Users')),
            ],
            options={
                'db_table': 'submit_record',
            },
        ),
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='API.Admins')),
                ('record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='API.UserRecord')),
            ],
            options={
                'db_table': 'send',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id1', models.ForeignKey(blank=True, db_column='admin_id1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='API.Admins')),
                ('user_id1', models.ForeignKey(blank=True, db_column='user_id1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='API.Users')),
            ],
            options={
                'db_table': 'search',
            },
        ),
    ]
