from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

from .views import (
    TweetDetailView,
    TweetListView,
    TweetUpdateView,
    TweetCreateView, #tweet_create_view
    TweetDeleteView,
    )

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search$', TweetListView.as_view(), name="list"),
    url(r'^create/', TweetCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"),
]


