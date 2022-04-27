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
   # new route used to show a form and create a shark
   path('sharks/create/', views.SharkCreate.as_view(), name='sharks_create'),
   path('sharks/<int:pk>/update/', views.SharkUpdate.as_view(), name='sharks_update'),
   path('sharks/<int:pk>/delete/', views.SharkDelete.as_view(), name='sharks_delete'),
]