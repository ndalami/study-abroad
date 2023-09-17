from django.urls import path
from . import views

app_name='mybog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('university', views.university, name='university'),
    path('apply', views.apply, name='apply'),
    path('blog', views.blog, name='blog'),
    path('blogdetail/<post_id>', views.blogdetail, name='blogdetail'),
]
