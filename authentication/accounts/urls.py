from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_register/', views.student_reg_view, name='student_reg'),
    path('student_login/', views.student_login_view, name='student_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student_login/dashboard/', views.dashboard, name='student_dashboard'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/edit_profile/', views.edit_profile_student, name='edit_profile'),

    path('student_login/change_password/',views.change_password,name='change_password'),
    path('change_password/',views.change_password,name='change_password')
]
