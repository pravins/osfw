from django.db import models

# Create your models here.
class Osfw(models.Model):
	familyname = models.CharField(max_length=35)
	subfamily = models.CharField(max_length=35)
	version = models.CharField(max_length=100)
	license = models.CharField(max_length=1000)
	upstreamurl = models.CharField(max_length=300)
	langsupport = models.CharField(max_length=1000)
	scriptsupport = models.CharField(max_length=1000)
	ttffilename = models.CharField(max_length=100)
	copyright = models.CharField(max_length=1000)
	likes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.familyname
