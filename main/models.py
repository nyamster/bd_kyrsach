# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bar(models.Model):
    bar_id = models.AutoField(primary_key=True)
    gain = models.ForeignKey('Gain', models.DO_NOTHING)
    earnings = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bar'


class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    shedule = models.ForeignKey('Shedule', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'club'




class Gain(models.Model):
    gain_id = models.AutoField(primary_key=True)
    earnings = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gain'


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    food = models.TextField()
    drinks = models.TextField()

    class Meta:
        managed = False
        db_table = 'menu'


class Requesite(models.Model):
    requesite_id = models.AutoField(primary_key=True)
    name = models.TextField()
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'requesite'


class Security(models.Model):
    stuff = models.OneToOneField('Stuff', models.DO_NOTHING, primary_key=True)
    violation = models.ForeignKey('Violation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'security'



class Stuff(models.Model):
    stuff_id = models.AutoField(primary_key=True)
    name = models.TextField()
    post = models.TextField()
    salary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stuff'

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.TextField()
    ticket_price = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    menu = models.ForeignKey('Menu', models.DO_NOTHING)
    gain = models.ForeignKey('Gain', models.DO_NOTHING)

    requesites = models.ManyToManyField(Requesite)
    stuffs = models.ManyToManyField(Stuff)
    class Meta:
        managed = False
        db_table = 'event'

class Shedule(models.Model):
    shedule_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    time = models.DateField()

    class Meta:
        managed = False
        db_table = 'shedule'

class Violation(models.Model):
    violation_id = models.AutoField(primary_key=True)
    visitor = models.ForeignKey('Visitor', models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'violation'


class Visitor(models.Model):
    visitor_id = models.AutoField(primary_key=True)
    name = models.TextField()
    age = models.IntegerField(blank=True, null=True)
    sex = models.TextField()
    allergies = models.TextField()
    cash = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'visitor'


class VisitorEvent(models.Model):
    visitor_event_id = models.AutoField(primary_key=True)
    visitor = models.ForeignKey(Stuff, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitor_event'

class EventRequesites(models.Model):
    requesite_event_id = models.AutoField(primary_key=True)
    requesite = models.ForeignKey(Requesite, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_requesites'


class EventStuffs(models.Model):
    stuff_event_id = models.AutoField(primary_key=True)
    stuff = models.ForeignKey(Stuff, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_stuffs'