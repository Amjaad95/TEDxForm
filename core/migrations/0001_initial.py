# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regestiration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(default=b'', max_length=1, verbose_name='\u0627\u0644\u062c\u0646\u062f\u0631', choices=[(b'F', '\u0623\u0646\u062b\u0649'), (b'M', '\u0630\u0643\u0631')])),
                ('age', models.IntegerField(default=0)),
                ('mobile', models.CharField(max_length=20)),
                ('emial', models.EmailField(max_length=100)),
                ('city', models.CharField(default='\u0627\u0644\u0631\u064a\u0627\u0636', max_length=1, verbose_name='\u0627\u0644\u0645\u062f\u064a\u0646\u0629')),
                ('fromNGH', models.BooleanField(default=True)),
                ('job_title', models.CharField(max_length=100)),
                ('yourself', models.TextField()),
                ('about_tedx', models.TextField()),
                ('attend_Tedx', models.BooleanField(default=True)),
                ('past_experience', models.TextField()),
                ('referral', models.CharField(max_length=20)),
                ('expectations', models.TextField()),
                ('meaning', models.TextField()),
                ('interview', models.BooleanField(default=True)),
                ('take_pic', models.BooleanField(default=True)),
                ('your_interest', models.CharField(max_length=50, choices=[(b'A', '\u0627\u0644\u0641\u0646'), (b'E', '\u0627\u0644\u062a\u0639\u0644\u064a\u0645'), (b'H', '\u0627\u0644\u0635\u062d\u0629'), (b'T', '\u0627\u0644\u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627'), (b'S', '\u0627\u0644\u0631\u064a\u0627\u0636\u0629'), (b'B', '\u0631\u064a\u0627\u062f\u0629 \u0627\u0644\u0623\u0639\u0645\u0627\u0644'), (b'V', '\u0627\u0644\u062a\u0637\u0648\u0639'), (b'M', '\u0627\u0644\u062a\u0633\u0648\u064a\u0642'), (b'L', '\u0627\u0644\u0623\u062f\u0628')])),
                ('submission', models.DateTimeField(auto_now=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0625\u0631\u0633\u0627\u0644')),
                ('modification', models.DateTimeField(auto_now=True, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0625\u0631\u0633\u0627\u0644')),
            ],
        ),
    ]
