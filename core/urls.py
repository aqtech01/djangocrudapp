from django.urls import path
from core.views import *

urlpatterns = [
    path('',index,name="index"),
    path('inser_data',insertData,name="insertData"),
    path('update/<id>',updateData,name="updateData"),
    path('delete/<id>',deleteData,name="deleteData"),
]
