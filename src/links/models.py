from django.conf import settings
from django.db import models
from django.urls import reverse

from .utils import link_generator, create_shortlink

# Create your models here.
class Link(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	link_web 	= models.CharField(max_length=255, blank=True)
	shortlink 	= models.CharField(max_length=255, blank=True)
	status 		= models.BooleanField(default=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if self.shortlink is None or self.shortlink == "":
			self.shortlink = create_shortlink(self)
		if not "http" in self.link_web:
			self.link_web = "http://" + self.link_web
		super().save(*args, **kwargs)

	def __str__(self):
		return self.link_web

	def get_shortlink(self):
		link_path = reverse("shortlink", kwargs={"shortlink": self.shortlink})
		return link_path