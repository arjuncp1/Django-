from django.contrib import admin
from django.urls import path, include
from user.views import *

urlpatterns = [
    path('home/', UserHome.as_view(), name='uhome'),
    path('adpat/', PatientView.as_view(), name='adpat'),
    path('plist/', PatientListView.as_view(), name='plist'),
    path('patdel/<int:pid>', PatientRemoveView.as_view(), name='pdel'),
    path('editpat/<int:pid>', EditPatientView.as_view(), name='pedit'),
    path('adddmed/', AddMedincine.as_view(), name='amed'),
    path('mlist/', MedicineListView.as_view(), name='mlist'),








]