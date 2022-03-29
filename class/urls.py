from django.urls import path
from .views import Studecreate, Studedetail, Studlist, studeDelete, studeupdate


app_name='class'


urlpatterns = [
    path('',Studlist.as_view(),name='students'),
    path('create/',Studecreate.as_view(),name='create-view'),
    path('detail/<int:pk>/',Studedetail.as_view(),name='detail-view'),
    path('update/<int:pk>/', studeupdate.as_view(), name='update-view'),
    path('delete/<int:pk>/',studeDelete.as_view(),name='delete-view')
 
]
