from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('record/<int:primaryKey>', views.customer_record, name='record'),
    path('delete_record/<int:primaryKey', views.delete_record, name='delete_record')
]
