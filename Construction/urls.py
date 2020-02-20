from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('pricing/', views.pricing, name='pricing'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('projects/', views.projects, name='projects'),
    path('projects-single/', views.project, name='projects-single'),
    path('news/', views.news, name='news'),
    path('news-left/', views.news2, name='news-left'),
    path('projects/gallery/', views.gallery, name='gallery'),
    path('projects/gallery2/', views.gallery2, name='gallery2'),
]