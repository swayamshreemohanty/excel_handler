from django.urls import path

from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('update_emp',views.update_emp,name='update_emp'),
    path('fetch_emp_by_id',views.fetch_emp_by_id,name='fetch_emp_by_id'),
    path('fetch_all_emp',views.fetch_all_emp,name='fetch_all_emp'),
    path('get_csrf_token',views.get_csrf_token,name='get_csrf_token'),
]
