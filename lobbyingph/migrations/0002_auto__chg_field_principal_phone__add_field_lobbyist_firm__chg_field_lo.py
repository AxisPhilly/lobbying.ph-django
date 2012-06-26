# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Principal.phone'
        db.alter_column('lobbyingph_principal', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12))
        # Adding field 'Lobbyist.firm'
        db.add_column('lobbyingph_lobbyist', 'firm',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Firm'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'Lobbyist.phone'
        db.alter_column('lobbyingph_lobbyist', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'Firm.phone'
        db.alter_column('lobbyingph_firm', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12))

    def backwards(self, orm):

        # Changing field 'Principal.phone'
        db.alter_column('lobbyingph_principal', 'phone', self.gf('django.db.models.fields.CharField')(max_length=10))
        # Deleting field 'Lobbyist.firm'
        db.delete_column('lobbyingph_lobbyist', 'firm_id')


        # Changing field 'Lobbyist.phone'
        db.alter_column('lobbyingph_lobbyist', 'phone', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Firm.phone'
        db.alter_column('lobbyingph_firm', 'phone', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        'lobbyingph.firm': {
            'Meta': {'object_name': 'Firm'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'lobbyingph.lobbyist': {
            'Meta': {'object_name': 'Lobbyist'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Firm']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'lobbyingph.principal': {
            'Meta': {'object_name': 'Principal'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['lobbyingph']