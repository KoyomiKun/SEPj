from django.db import models


# Create your models here.


class Admins(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=10)
    admin_email = models.CharField(max_length=32, blank=True, null=True)
    admin_record = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'admins'


class Search(models.Model):
    admin_id1 = models.ForeignKey(Admins, models.DO_NOTHING, db_column='admin_id1', blank=True, null=True)
    user_id1 = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_id1', blank=True, null=True)

    class Meta:
        db_table = 'search'


class Send(models.Model):
    admin = models.ForeignKey(Admins, models.DO_NOTHING, blank=True, null=True)
    record = models.ForeignKey('UserRecord', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'send'


class SubmitRecord(models.Model):
    user_id2 = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_id2', blank=True, null=True)
    record_id1 = models.ForeignKey('UserRecord', models.DO_NOTHING, db_column='record_id1', blank=True, null=True)

    class Meta:
        db_table = 'submit_record'


class UserRecord(models.Model):
    record_id = models.CharField(primary_key=True, max_length=8)
    record_time = models.DateField(blank=True, null=True)
    record_start = models.CharField(max_length=30, blank=True, null=True)
    record_end = models.CharField(max_length=30, blank=True, null=True)
    record_condition = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_record'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    user_name = models.CharField(max_length=16)
    user_email = models.CharField(max_length=32, blank=True, null=True)
    user_phone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'users_'
