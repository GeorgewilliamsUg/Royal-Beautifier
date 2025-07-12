from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('events/', views.events, name='events'),
    path('coaching/', views.coaching, name='coaching'),
    path('mentorship/', views.mentorship, name='mentorship'),
    path('etiquette-training/', views.etiquette_training, name='etiquette_training'),
    path('counseling/', views.counseling, name='counseling'),
    path('speaking/', views.speaking, name='speaking'),
]