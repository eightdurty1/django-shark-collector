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
   path('sharks/<int:shark_id>/add_feeding/', views.add_feeding, name='add_feeding'),
   path('sharks/<int:shark_id>/assoc_toy/<int:shark_id>/', views.assoc_toy, name='assoc_toy'),
   path('toys/', views.ToyList.as_view(), name='toys_index'),
   path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
   path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
   path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
   path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]