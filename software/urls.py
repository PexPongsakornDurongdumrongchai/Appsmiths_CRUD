from django.urls import path

from . import views

urlpatterns = [
    path('', views.SoftwareList.as_view(), name='software_list'),
    path('new', views.SoftwareCreate.as_view(), name='software_new'),
    path('view/<int:pk>', views.SoftwareView.as_view(), name='software_view'),
    path('edit/<int:pk>', views.SoftwareUpdate.as_view(), name='software_edit'),
    path('delete/<int:pk>', views.SoftwareDelete.as_view(), name='software_delete'),
]