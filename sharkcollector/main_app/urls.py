from django.contrib import admin
# Add the include function to the import
from django.urls import path
from . import views

# route setup
urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('sharks/', views.sharks_index, name='index'),
   path('sharks/<int:shark_id>/', views.sharks_detail, name='detail'),
]