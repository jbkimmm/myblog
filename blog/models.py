from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_save

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'pk': self.pk})

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, default=True)
    image = models.ImageField(upload_to='post_image', blank=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


def __unicode__(self):
    return self.title

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse("posts:detail", kwargs={"slug": self.slug})

class Meta:
    ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):
    slug = slugify(instance.timestamp)
    # if new_slug is not None:
    #     slug = new_slug
    #     qs = Post.objects.filter(slug=slug).order_by("-id")
    #     exists = qs.exists()
    #     if exists:
    #         new_slug = "%s-%s" %(slug, qs.first().id)
    #         return create_slug(instance, new_slug=new_slug)
    return slug

'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''