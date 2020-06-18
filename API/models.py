# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PersonInfo(models.Model):
    email = models.CharField(primary_key=True, max_length=30)
    name = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    id = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_info'


class Register(models.Model):
    rid = models.IntegerField(primary_key=True)
    shift = models.ForeignKey('ShiftInfo', models.DO_NOTHING)
    email = models.ForeignKey(PersonInfo, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'register'


class ShiftInfo(models.Model):
    shift_id = models.CharField(primary_key=True, max_length=5)
    start = models.TextField()
    end = models.TextField()
    empty_ticket = models.IntegerField()
    risk_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shift_info'
