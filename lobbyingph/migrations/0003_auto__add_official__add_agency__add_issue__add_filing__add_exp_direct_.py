# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Official'
        db.create_table('lobbyingph_official', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('lobbyingph', ['Official'])

        # Adding model 'Agency'
        db.create_table('lobbyingph_agency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('lobbyingph', ['Agency'])

        # Adding model 'Issue'
        db.create_table('lobbyingph_issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('lobbyingph', ['Issue'])

        # Adding model 'Filing'
        db.create_table('lobbyingph_filing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quarter', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('total_exp_direct_comm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('total_exp_indriect_comm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('total_exp_other', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('principal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Principal'], null=True, blank=True)),
        ))
        db.send_create_signal('lobbyingph', ['Filing'])

        # Adding M2M table for field firms on 'Filing'
        db.create_table('lobbyingph_filing_firms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('filing', models.ForeignKey(orm['lobbyingph.filing'], null=False)),
            ('firm', models.ForeignKey(orm['lobbyingph.firm'], null=False))
        ))
        db.create_unique('lobbyingph_filing_firms', ['filing_id', 'firm_id'])

        # Adding M2M table for field lobbyists on 'Filing'
        db.create_table('lobbyingph_filing_lobbyists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('filing', models.ForeignKey(orm['lobbyingph.filing'], null=False)),
            ('lobbyist', models.ForeignKey(orm['lobbyingph.lobbyist'], null=False))
        ))
        db.create_unique('lobbyingph_filing_lobbyists', ['filing_id', 'lobbyist_id'])

        # Adding model 'Exp_Direct_Comm'
        db.create_table('lobbyingph_exp_direct_comm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Category'])),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Issue'], null=True, blank=True)),
            ('bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Bill'], null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('other_desc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('official', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Official'], null=True, blank=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Agency'], null=True, blank=True)),
            ('quarter', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('filing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Filing'])),
        ))
        db.send_create_signal('lobbyingph', ['Exp_Direct_Comm'])

        # Adding model 'Exp_Other'
        db.create_table('lobbyingph_exp_other', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Filing'])),
        ))
        db.send_create_signal('lobbyingph', ['Exp_Other'])

        # Adding model 'Bill'
        db.create_table('lobbyingph_bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal('lobbyingph', ['Bill'])

        # Adding model 'Exp_Indirect_Comm'
        db.create_table('lobbyingph_exp_indirect_comm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Category'])),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Issue'], null=True, blank=True)),
            ('bill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Bill'], null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('other_desc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('official', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Official'], null=True, blank=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Agency'], null=True, blank=True)),
            ('quarter', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('filing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lobbyingph.Filing'])),
        ))
        db.send_create_signal('lobbyingph', ['Exp_Indirect_Comm'])

        # Adding model 'Category'
        db.create_table('lobbyingph_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('lobbyingph', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Official'
        db.delete_table('lobbyingph_official')

        # Deleting model 'Agency'
        db.delete_table('lobbyingph_agency')

        # Deleting model 'Issue'
        db.delete_table('lobbyingph_issue')

        # Deleting model 'Filing'
        db.delete_table('lobbyingph_filing')

        # Removing M2M table for field firms on 'Filing'
        db.delete_table('lobbyingph_filing_firms')

        # Removing M2M table for field lobbyists on 'Filing'
        db.delete_table('lobbyingph_filing_lobbyists')

        # Deleting model 'Exp_Direct_Comm'
        db.delete_table('lobbyingph_exp_direct_comm')

        # Deleting model 'Exp_Other'
        db.delete_table('lobbyingph_exp_other')

        # Deleting model 'Bill'
        db.delete_table('lobbyingph_bill')

        # Deleting model 'Exp_Indirect_Comm'
        db.delete_table('lobbyingph_exp_indirect_comm')

        # Deleting model 'Category'
        db.delete_table('lobbyingph_category')


    models = {
        'lobbyingph.agency': {
            'Meta': {'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lobbyingph.bill': {
            'Meta': {'object_name': 'Bill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'lobbyingph.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lobbyingph.exp_direct_comm': {
            'Meta': {'object_name': 'Exp_Direct_Comm'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Agency']", 'null': 'True', 'blank': 'True'}),
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Bill']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Category']"}),
            'filing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Filing']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Issue']", 'null': 'True', 'blank': 'True'}),
            'official': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Official']", 'null': 'True', 'blank': 'True'}),
            'other_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'lobbyingph.exp_indirect_comm': {
            'Meta': {'object_name': 'Exp_Indirect_Comm'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Agency']", 'null': 'True', 'blank': 'True'}),
            'bill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Bill']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Category']"}),
            'filing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Filing']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Issue']", 'null': 'True', 'blank': 'True'}),
            'official': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Official']", 'null': 'True', 'blank': 'True'}),
            'other_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.SmallIntegerField', [], {}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'lobbyingph.exp_other': {
            'Meta': {'object_name': 'Exp_Other'},
            'filing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Filing']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lobbyingph.filing': {
            'Meta': {'object_name': 'Filing'},
            'firms': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Firm']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lobbyists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lobbyingph.Lobbyist']", 'null': 'True', 'blank': 'True'}),
            'principal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lobbyingph.Principal']", 'null': 'True', 'blank': 'True'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'total_exp_direct_comm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'total_exp_indriect_comm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'total_exp_other': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
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
        'lobbyingph.issue': {
            'Meta': {'object_name': 'Issue'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'lobbyingph.official': {
            'Meta': {'object_name': 'Official'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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