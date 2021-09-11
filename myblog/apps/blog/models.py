from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock


class BlogCategory(TimeStampedModel):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    thumbnail = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:view_blogs_by_category', kwargs={'slug': self.slug})


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT)

    image = models.ImageField(upload_to='images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/thumbnail', blank=True, null=True)

    is_published = models.BooleanField(default=False)
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock(features=[
            'h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'code', 'superscript', 'subscript', 'strikethrough',
            'blockquote', 'link', 'document-link', 'image', 'embed', 'ol', 'ul'
        ])),
        ('code', CodeBlock()),
        ('image', ImageChooserBlock()),
    ])

    meta_keyword = models.CharField(max_length=256, blank=True, null=True)
    meta_description = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:view_blog_detail', kwargs={'slug': self.slug})
