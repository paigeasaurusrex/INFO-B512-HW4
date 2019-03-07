# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Projects(models.Model):
    Project_ID=models.IntegerField(primary_key=True)
    Project_Descrip=models.CharField(max_length=500)
    Project_year=models.IntegerField(null=True)
    def __str__(self):
        return '%s %s %d' % (self.Project_ID, self.Project_Descrip, self.Project_year)
        
        
@python_2_unicode_compatible
class Skills(models.Model):
    Skill_ID=models.IntegerField(primary_key=True)
    Skill_Descrip=models.CharField(max_length=500)
    Skill_rank=models.IntegerField(null=True)
    def __str__(self):
        return '%s %s %d' % (self.Skill_ID, self.Skill_Descrip, self.Skill_rank)
        