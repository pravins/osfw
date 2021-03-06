from django.db import models

# Create your models here.
class Osfw(models.Model):
	familyname = models.CharField(max_length=35)
	description = models.CharField(max_length=1000)
	subfamily = models.CharField(max_length=35)
	version = models.CharField(max_length=50)
	license = models.CharField(max_length=1000)
	upstreamurl = models.CharField(max_length=100)
	langsupport = models.CharField(max_length=1000)
	scriptsupport = models.CharField(max_length=200)
	ttffilename = models.CharField(max_length=50)
	fontformat = models.CharField(max_length=30)
	copyright = models.CharField(max_length=1000)
        viewstring = models.CharField(max_length=600)
	glyphcount =  models.IntegerField(default=0)
	charactercount =  models.IntegerField(default=0)
	woffurl = models.CharField(max_length=200)
	likes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.familyname
