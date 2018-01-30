from django.contrib import admin

# Register your models here.
from .models import Tweet
from .forms import TweetModelForm


#admin form for tweet model in Admin section
#we are trying to replace this form with our very own modified form
class TweetModelAdmin(admin.ModelAdmin):
    #form = TweetModelForm
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetModelAdmin)
