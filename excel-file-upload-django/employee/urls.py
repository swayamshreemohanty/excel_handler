from django.urls import path  
from employee import views  

urlpatterns = [  
    path('', views.show),  
    path('storefile', views.storefile),  

    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
     
    #APIs methods url
    path('upload_excel', views.upload_excel),  
    path('add_emp', views.add_emp),  
    path('update_emp', views.update_emp),  
    path('fetch_all_emp', views.fetch_all_emp),  
    path('fetch_emp_by_id', views.fetch_emp_by_id),  
    
    # path('register', views.register),
    path('login', views.login),
    path('get_csrf_token',views.get_csrf_token,name='get_csrf_token'),
]  