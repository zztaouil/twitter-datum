from django.urls import path

from tweets import views

urlpatterns = [
    path('api/search', views.search, name='search'),
    path('api/facets', views.facets, name='facets'),
    path('api/pins', views.pins, name='pins'),
    path('api/pins/<str:tweet_id>', views.unpin, name='unpin'),
    path('api/analytics', views.analytics, name='analytics'),
]
