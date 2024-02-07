from django.urls import path
from .views import TemplView
urlpatterns = [
    path('template_landing/', TemplView.as_view(), name='template_landing'),
]