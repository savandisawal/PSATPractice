from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('approvals/', views.pending_approvals, name='pending_approvals'),
    path('approvals/<int:user_id>/approve/', views.approve_student, name='approve_student'),
]
