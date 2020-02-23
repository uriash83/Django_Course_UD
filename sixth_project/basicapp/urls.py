from django.conf.urls import url,include
from django.urls import path,re_path
from basicapp import views

app_name = 'basicapp' # to jest brane w basicappbase.html <a class="navbar-brand" href="{% url 'basicapp:list' %}">Schools</a>
urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete')
    #re_path(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail'),
    # url używamy do regex
]