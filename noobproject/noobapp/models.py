from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.slug, filename)

class friend(models.Model):
	slug = models.SlugField(unique=True)
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=120)
	Address = models.TextField(blank = True)
	Birthday = models.DateField(blank = True)
	#Image = models.ImageField(blank = True)
	Image = models.ImageField(upload_to = upload_location, null=True, blank = True)
	Email = models.EmailField(blank = True)

	def __unicode__(self):
		return self.Name
	def __str__(self):
		return self.Name
	def get_absolute_url(self):
		return reverse("friend:friend_detail", kwargs = {"slug":self.slug})
	class Meta:
		verbose_name = "Name List"

def create_slug(instance, new_slug=None):
	slug = slugify(instance.Name)
	if new_slug is not None:
		slug = new_slug
	qs = friend.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender,instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender = friend)