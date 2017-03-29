# -*- coding: utf-8  -*-
from django.db import models
import datetime

gender_choices = (
    ('F', u'أنثى'),
    ('M', u'ذكر'),
)


class Regestiration(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=gender_choices,
                              verbose_name=u"الجندر", default="")
    age = models.IntegerField(default=0)
    mobile = models.CharField(max_length=20)
    emial = models.EmailField(max_length=100)
    city = models.CharField(max_length=1,
                            verbose_name=u"المدينة", default=u"الرياض")
    fromNGH = models.BooleanField(default= True)
    job_title = models.CharField(max_length=100)
    yourself = models.TextField()
    about_tedx = models.TextField()
    attend_Tedx = models.BooleanField(default=True)
    past_experience = models.TextField()
    referral = models.CharField(max_length=20)
    expectations = models.TextField()
    meaning = models.TextField()
    interview = models.BooleanField(default=True)
    take_pic = models.BooleanField(default=True)
    interests_choices = (
        ('A', u'الفن'),
        ('E',u'التعليم'),
        ('H',u'الصحة'),
        ('T',u'التكنولوجيا'),
        ('S',u'الرياضة'),
        ('B',u'ريادة الأعمال'),
        ('V',u'التطوع'),
        ('M',u'التسويق'),
        ('L',u'الأدب'),

    )
    your_interest = models.CharField(max_length=50, choices=interests_choices)
    submission = models.DateTimeField(u'تاريخ الإرسال', auto_now=True)
    modification = models.DateTimeField(u'تاريخ الإرسال', auto_now=True)
