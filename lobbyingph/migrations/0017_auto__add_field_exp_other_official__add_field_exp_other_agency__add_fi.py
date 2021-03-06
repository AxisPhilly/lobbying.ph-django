# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Exp_Other.official'
        db.add_column('lobbyingph_exp_other', 'official',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Official'], null=True),
                      keep_default=False)

        # Adding field 'Exp_Other.agency'
        db.add_column('lobbyingph_exp_other', 'agency',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Agency'], null=True),
                      keep_default=False)

        # Adding field 'Exp_Other.description'
        db.add_column('lobbyingph_exp_other', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Exp_Other.value'
        db.add_column('lobbyingph_exp_other', 'value',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=12, decimal_places=2),
                      keep_default=False)

        # Adding field 'Exp_Other.date'
        db.add_column('lobbyingph_exp_other', 'date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Exp_Other.place'
        db.add_column('lobbyingph_exp_other', 'place',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Exp_Other.source'
        db.add_column('lobbyingph_exp_other', 'source',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Principal'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Exp_Other.official'
        db.delete_column('lobbyingph_exp_other', 'official_id')

        # Deleting field 'Exp_Other.agency'
        db.delete_column('lobbyingph_exp_other', 'agency_id')

        # Deleting field 'Exp_Other.description'
        db.delete_column('lobbyingph_exp_other', 'description')

        # Deleting field 'Exp_Other.value'
        db.delete_column('lobbyingph_exp_other', 'value')

        # Deleting field 'Exp_Other.date'
        db.delete_column('lobbyingph_exp_other', 'date')

        # Deleting field 'Exp_Other.place'
        db.delete_column('lobbyingph_exp_other', 'place')

        # Deleting field 'Exp_Other.source'
        db.delete_column('lobbyingph_exp_other', 'source_id')


    models = {
        'lobbyingph.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lobbyingph.bill': {
            'Meta': {'ordering': "['number']", 'object_name': 'Bill'},
            'bill_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "'http://legislation.phila.gov/detailreport/?key='", 'max_length': '200'})
        },
        'lobbyingph.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lobbyingph.communication_method': {
            'Meta': {'ordering': "['name']", 'object_name': 'Communication_Method'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lobbyingph.exp_direct_comm': {
            'Meta': {'object_name': 'Exp_Direct_Comm'},
            'agencies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Agency']", 'null': 'True', 'blank': 'True'}),
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Bill']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Category']"}),
            'filing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Filing']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Issue']", 'null': 'True', 'blank': 'True'}),
            'officials': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Official']", 'null': 'True', 'blank': 'True'}),
            'other_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'lobbyingph.exp_indirect_comm': {
            'Meta': {'object_name': 'Exp_Indirect_Comm'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Agency']", 'null': 'True', 'blank': 'True'}),
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Bill']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Category']"}),
            'filing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Filing']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Receipent_Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Issue']", 'null': 'True', 'blank': 'True'}),
            'methods': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Communication_Method']", 'null': 'True', 'blank': 'True'}),
            'officials': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Official']", 'null': 'True', 'blank': 'True'}),
            'other_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'lobbyingph.exp_other': {
            'Meta': {'object_name': 'Exp_Other'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Agency']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'filing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Filing']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'official': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Official']", 'null': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Principal']", 'null': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'})
        },
        'lobbyingph.filing': {
            'Meta': {'object_name': 'Filing'},
            'firms': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Firm']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lobbyists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Lobbyist']", 'null': 'True', 'blank': 'True'}),
            'principal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Principal']", 'null': 'True', 'blank': 'True'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'total_exp_direct_comm': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'}),
            'total_exp_indirect_comm': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'}),
            'total_exp_other': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'}),
            'year': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'})
        },
        'lobbyingph.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm'},
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
        'lobbyingph.issue': {
            'Meta': {'ordering': "['description']", 'object_name': 'Issue'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lobbyingph.lobbyist': {
            'Meta': {'ordering': "['name']", 'object_name': 'Lobbyist'},
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
        'lobbyingph.official': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Official'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Agency']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'lobbyingph.principal': {
            'Meta': {'ordering': "['name']", 'object_name': 'Principal'},
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
        'lobbyingph.receipent_group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Receipent_Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lobbyingph']