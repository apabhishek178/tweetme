from django.conf import settings
from django.db import models
from .validators import validate_content
from django.core.urlresolvers import reverse
# Create your models here.
class Tweet(models.Model):
    #user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    #content with the inline validators
    content = models.CharField(max_length=140, validators=[validate_content])

    # auto_now_add will automatically gonna add time to the time stamp when the tweet is updated
    updated = models.DateField(auto_now=True)
    #auto_now_add will automatically gonna add time to the time stamp when the tweet is made
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})
