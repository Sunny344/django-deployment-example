from django.urls import path
from my_users import views

app_name = 'my_users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
