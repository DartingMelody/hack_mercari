# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table(u'WebUI_customuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('contact_number', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
        ))
        db.send_create_signal(u'WebUI', ['CustomUser'])

        # Adding model 'Trip'
        db.create_table(u'WebUI_trip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hosts trip', to=orm['WebUI.CustomUser'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('cluster', self.gf('django.db.models.fields.TextField')()),
            ('travel_distance', self.gf('django.db.models.fields.FloatField')()),
            ('start_place', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('end_place', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'WebUI', ['Trip'])

        # Adding M2M table for field participants on 'Trip'
        m2m_table_name = db.shorten_name(u'WebUI_trip_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trip', models.ForeignKey(orm[u'WebUI.trip'], null=False)),
            ('customuser', models.ForeignKey(orm[u'WebUI.customuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trip_id', 'customuser_id'])

        # Adding model 'Request'
        db.create_table(u'WebUI_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['WebUI.CustomUser'])),
            ('trip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['WebUI.Trip'])),
            ('start_lat', self.gf('django.db.models.fields.FloatField')()),
            ('start_lng', self.gf('django.db.models.fields.FloatField')()),
            ('end_lat', self.gf('django.db.models.fields.FloatField')()),
            ('end_lng', self.gf('django.db.models.fields.FloatField')()),
            ('start_place', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('end_place', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'WebUI', ['Request'])


    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table(u'WebUI_customuser')

        # Deleting model 'Trip'
        db.delete_table(u'WebUI_trip')

        # Removing M2M table for field participants on 'Trip'
        db.delete_table(db.shorten_name(u'WebUI_trip_participants'))

        # Deleting model 'Request'
        db.delete_table(u'WebUI_request')


    models = {
        u'WebUI.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'contact_number': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'WebUI.request': {
            'Meta': {'object_name': 'Request'},
            'end_lat': ('django.db.models.fields.FloatField', [], {}),
            'end_lng': ('django.db.models.fields.FloatField', [], {}),
            'end_place': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['WebUI.CustomUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_lat': ('django.db.models.fields.FloatField', [], {}),
            'start_lng': ('django.db.models.fields.FloatField', [], {}),
            'start_place': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['WebUI.Trip']"})
        },
        u'WebUI.trip': {
            'Meta': {'object_name': 'Trip'},
            'cluster': ('django.db.models.fields.TextField', [], {}),
            'end_place': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'are participants in Trip'", 'blank': 'True', 'to': u"orm['WebUI.CustomUser']"}),
            'start_place': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'travel_distance': ('django.db.models.fields.FloatField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts trip'", 'to': u"orm['WebUI.CustomUser']"})
        }
    }

    complete_apps = ['WebUI']