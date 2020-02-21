from basicapp import views
from django.urls import path,re_path

app_name = 'basicapp'

urlpatterns = [
    re_path(r'^register/$', views.register , name='register' ),
    path('user_login/',views.user_login,name='user_login'),
]