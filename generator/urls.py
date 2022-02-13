from django.urls import path
from .views import (SchemeListView, SchemeCreateView, SchemeUpdateView, SchemeDeleteView, DatasetListView, 
            SchemeColumnCreateView, SchemeColumnUpdateView, SchemeColumnDeleteView, SchemeColumnListView, generate_csv)

urlpatterns = [
    path('scheme_list/', SchemeListView.as_view(), name='scheme-list'),
    path('scheme/add/', SchemeCreateView.as_view(), name='scheme-add'),
    path('scheme/<int:pk>/', SchemeUpdateView.as_view(), name='scheme-update'),
    path('scheme/<int:pk>/delete/', SchemeDeleteView.as_view(), name='scheme-delete'),

    path('scheme/column/list/<int:scheme__id>', SchemeColumnListView.as_view(), name='scheme-column-list'),
    path('scheme/column/add/', SchemeColumnCreateView.as_view(), name='scheme-column-add'),
    path('scheme/column/<int:pk>/', SchemeColumnUpdateView.as_view(), name='scheme-column-update'),
    path('scheme/column/<int:pk>/delete/', SchemeColumnDeleteView.as_view(), name='scheme-column-delete'),


    path('dataset_list/', DatasetListView.as_view(), name='dataset-list'),
    path('dataset/<int:pk>/generate/', generate_csv, name='generate-dataset'),
]