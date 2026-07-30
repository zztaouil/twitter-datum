from django.urls import path

from tweets import views

urlpatterns = [
    path('api/search', views.search, name='search'),
    path('api/facets', views.facets, name='facets'),
    path('api/pins', views.pins, name='pins'),
    path('api/pins/<str:tweet_id>', views.unpin, name='unpin'),
    path('api/analytics', views.analytics, name='analytics'),
    path('api/analytics/coverage', views.coverage, name='coverage'),
    path('api/analytics/media-backfill', views.media_backfill, name='media_backfill'),
    path('api/analytics/reply-depth', views.reply_depth, name='reply_depth'),
]
