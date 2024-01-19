from django.urls import path
from . import views

urlpatterns = [
    path('',views.frontpage,name="frontpage"),
    path('create/',views.Create,name="create"),
    path('createstd',views.Addstd,name="add"),
    path('update/<int:id>/',views.Update,name="update"),
    path('updaterecord/<int:id>/',views.recUpdate,name="recupdate"),
    path('delete/<int:id>/',views.Delete,name="delete"),



]