# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteConfiguration'
        db.create_table(u'theme_siteconfiguration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('color_scheme', self.gf('django.db.models.fields.PositiveIntegerField')(default=3)),
            ('sidebar_alignment', self.gf('django.db.models.fields.CharField')(default='RI', max_length=2)),
            ('default_sidebar', self.gf('django.db.models.fields.TextField')()),
            ('blog_layout', self.gf('django.db.models.fields.PositiveIntegerField')(default=2)),
            ('footer_description', self.gf('mezzanine.core.fields.RichTextField')()),
            ('footer_blog_heading', self.gf('django.db.models.fields.CharField')(default='Recent posts', max_length=100)),
            ('footer_menu_heading', self.gf('django.db.models.fields.CharField')(default='Popular pages', max_length=100)),
            ('footer_flickr_heading', self.gf('django.db.models.fields.CharField')(default='Flickr photos', max_length=100)),
        ))
        db.send_create_signal(u'theme', ['SiteConfiguration'])


    def backwards(self, orm):
        # Deleting model 'SiteConfiguration'
        db.delete_table(u'theme_siteconfiguration')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'galleries.gallery': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Gallery', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'zip_import': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'pages.page': {
            'Meta': {'ordering': "('titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.homepage': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'breakout_button_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'breakout_content': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'breakout_heading': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'breaktou_button_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'featured_gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['galleries.Gallery']", 'null': 'True', 'blank': 'True'}),
            'featured_gallery_heading': ('django.db.models.fields.CharField', [], {'default': "'Our clients'", 'max_length': '100', 'blank': 'True'}),
            'featured_portfolio_heading': ('django.db.models.fields.CharField', [], {'default': "'Recent works'", 'max_length': '100', 'blank': 'True'}),
            'icon_box_layout': ('django.db.models.fields.CharField', [], {'default': "'TH'", 'max_length': '2'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'recent_blog_heading': ('django.db.models.fields.CharField', [], {'default': "'Latest blog posts'", 'max_length': '100', 'blank': 'True'})
        },
        u'theme.iconbox': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'IconBox'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boxes'", 'to': u"orm['theme.HomePage']"}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'theme.siteconfiguration': {
            'Meta': {'object_name': 'SiteConfiguration'},
            'blog_layout': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'color_scheme': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3'}),
            'default_sidebar': ('django.db.models.fields.TextField', [], {}),
            'footer_blog_heading': ('django.db.models.fields.CharField', [], {'default': "'Recent posts'", 'max_length': '100'}),
            'footer_description': ('mezzanine.core.fields.RichTextField', [], {}),
            'footer_flickr_heading': ('django.db.models.fields.CharField', [], {'default': "'Flickr photos'", 'max_length': '100'}),
            'footer_menu_heading': ('django.db.models.fields.CharField', [], {'default': "'Popular pages'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sidebar_alignment': ('django.db.models.fields.CharField', [], {'default': "'RI'", 'max_length': '2'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'theme.slide': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'background': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'blank': 'True'}),
            'button_link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'button_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'custom': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'blank': 'True'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['theme']