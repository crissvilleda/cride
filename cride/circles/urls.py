"""Circle Urls"""
#django
from django.urls import path

#views
from cride.circles.views import list_circles, create_circle

urlpatterns = [
  path('circles/',list_circles, name='listCircle'),
  path('circles/create/', create_circle, name='createCircle')
]