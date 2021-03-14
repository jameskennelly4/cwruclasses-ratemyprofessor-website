from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('class/<int:Class_id>', views.class_by_id, name='class_by_id'),
]
