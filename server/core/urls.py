from django.urls import path

from tweets import views

urlpatterns = [
    path('api/search', views.search, name='search'),
    path('api/facets', views.facets, name='facets'),
]
