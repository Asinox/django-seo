from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255, default="", blank=True)
    type = models.CharField(max_length=50, default="", blank=True)
    content = models.TextField(default="", blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('userapp_page_detail', [self.id], {})

    def __unicode__(self):
        return self.title or self.content