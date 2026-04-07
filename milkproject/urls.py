from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    
    path('', views.dashboard, name='dashboard'),
    path('custom-admin/', views.admin_dashboard, name='admin_dashboard'),
    path('farmer-home/', views.farmer_dashboard, name='farmer_dashboard'),
    
    path('register-farmer/', views.register_farmer, name='register_farmer'),
    path('delete-farmer/<int:user_id>/', views.delete_farmer, name='delete_farmer'),
    
    # NEW URL FOR EDITING
    path('edit-entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    path('edit-farmer/<int:user_id>/', views.edit_farmer, name='edit_farmer'),
    
   
   
]