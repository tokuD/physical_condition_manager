from django.urls import path
from . import views

app_name = 'body_temparature'

urlpatterns = [
    path('', views.UserList.as_view(), name='top'),
    path('detail/<int:pk>/', views.UserDetail.as_view(), name='detail'),
]
