from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_entry, name='add_entry'),
    path('delete/<int:id>/', views.delete_entry, name='delete_entry'),
    path('edit/<int:id>/', views.edit_entry, name='edit_entry'),
    path('export/', views.export_csv, name='export_csv'),

]
