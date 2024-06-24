from django.urls import path
from .views import home, chart

urlpatterns = [
    path('', home),
    path('chart', chart),
]