from django.urls import path
from .views import HomePageView, ServiceView, AboutView, PropertiesView, ContactView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('services/', ServiceView.as_view(), name='service'),
    path('about/', AboutView.as_view(), name='about'),
    path('properties/', PropertiesView.as_view(), name='properties'),
    path('contact/', ContactView.as_view(), name='contact'),
]
