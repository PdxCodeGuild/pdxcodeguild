# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
        ('galleries', '0002_auto_20141227_0224'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('question', models.CharField(max_length=300)),
                ('answer', mezzanine.core.fields.RichTextField()),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='FAQPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'FAQ page',
                'verbose_name_plural': 'FAQ pages',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('featured_portfolio_heading', models.CharField(default=b'Recent works', help_text=b'If present and featured_portfolio is set portfolio items will be shown with this header.', max_length=100, blank=True)),
                ('max_portfolio_items', models.PositiveIntegerField(default=6, help_text=b'The maximum number of items from the above selected portoflio to show.', null=True, blank=True)),
                ('icon_box_layout', models.CharField(default=b'TH', max_length=2, choices=[(b'TW', b'Two across'), (b'TH', b'Three across'), (b'TB', b'Three across boxes')])),
                ('recent_blog_heading', models.CharField(default=b'Latest blog posts', help_text=b'If present recent blog posts will be shown', max_length=100, blank=True)),
                ('breakout_heading', models.CharField(max_length=200, blank=True)),
                ('breakout_content', mezzanine.core.fields.RichTextField(blank=True)),
                ('breakout_button_text', models.CharField(max_length=200, blank=True)),
                ('breaktou_button_link', models.CharField(max_length=2000, blank=True)),
                ('featured_gallery_heading', models.CharField(default=b'Our clients', help_text=b'If present and featured_gallery is selected a carousel of the gallery images will be shown with this title.', max_length=100, blank=True)),
                ('featured_gallery', models.ForeignKey(blank=True, to='galleries.Gallery', null=True)),
                ('featured_portfolio', models.ForeignKey(blank=True, to='portfolio.Portfolio', null=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='IconBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', models.CharField(help_text=b'Enter the name of a font awesome icon, i.e. fa-eye. A list is available here http://fontawesome.io/', max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('content', mezzanine.core.fields.RichTextField()),
                ('link', models.CharField(help_text=b'Optional, if provided clicking the box will go here.', max_length=2000, blank=True)),
                ('homepage', models.ForeignKey(related_name='boxes', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color_scheme', models.PositiveIntegerField(default=3, help_text=b'Use the cog icon in the front end to try out color schemes.')),
                ('sidebar_alignment', models.CharField(default=b'RI', help_text=b'For pages that have a sidebar, determines if it is on the left or right', max_length=2, choices=[(b'LE', 'Left'), (b'RI', 'Right')])),
                ('default_sidebar', models.TextField()),
                ('blog_layout', models.PositiveIntegerField(default=2, help_text=b'Determines how many blog posts are shown per row in the blog list view', choices=[(1, 'One'), (2, 'Two')])),
                ('footer_description', mezzanine.core.fields.RichTextField()),
                ('footer_blog_heading', models.CharField(default=b'Recent posts', max_length=100)),
                ('footer_menu_heading', models.CharField(default=b'Popular pages', max_length=100)),
                ('footer_flickr_heading', models.CharField(default=b'Flickr photos', max_length=100)),
                ('footer_flickr_content', mezzanine.core.fields.RichTextField(help_text=b'If present will override the flickr widget in the footer', blank=True)),
                ('contact_iframe', models.TextField(help_text=b"If present any form with slug contact will displayed with a custom template that has this iframe at the top. i.e. add a Google Map's iframe here.", blank=True)),
                ('contact_iframe_layout', models.CharField(default=b'FULL', max_length=4, blank=True, choices=[(b'FULL', 'Full width'), (b'PAGE', 'Page width')])),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Site Configuration',
                'verbose_name_plural': 'Site Configuration',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('background', mezzanine.core.fields.FileField(max_length=255, verbose_name='Background Image', blank=True)),
                ('heading', models.CharField(max_length=100, blank=True)),
                ('subheading', models.CharField(max_length=100, blank=True)),
                ('content', models.TextField(help_text=b'Add <br> for line breaks', blank=True)),
                ('button_text', models.CharField(help_text=b'Optional, if present a button with the link specified below will be in the slide', max_length=100, blank=True)),
                ('button_link', models.CharField(max_length=2000, blank=True)),
                ('image', mezzanine.core.fields.FileField(max_length=255, verbose_name='Image', blank=True)),
                ('custom', models.TextField(help_text=b'Create a custom slide, everything else will be overriden', blank=True)),
                ('homepage', models.ForeignKey(related_name='slides', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.AddField(
            model_name='faq',
            name='faqpage',
            field=models.ForeignKey(related_name='faqs', to='theme.FAQPage'),
        ),
    ]
