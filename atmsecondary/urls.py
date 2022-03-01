from django.urls import path
from . import views
# from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_view, name='login'),
    path('logout', views.log_out, name='logout'),
    path('signup',views.signup, name='signup'),
    path('dashboard',views.dashboard, name='dashboard'),
    
    path('add-teacher', views.add_teacher, name='add_teacher'),
    path('view-teacher', views.view_teacher, name='view_teacher'),
    path('update-teacher/<id>/', views.update_teacher, name='update_teacher'),
    path('delete-teacher/<id>/', views.delete_teacher, name='delete_teacher'),
    
    path('add-subject', views.add_subject, name='add_subject'),
    path('view-subject', views.view_subject, name='view_subject'),
    path('update-subject/<id>/', views.update_subject, name='update_subject'),
    path('delete-subject/<id>/', views.delete_subject, name='delete_subject'),
    
    path('add-classroom', views.add_classroom, name='add_classroom'),
    path('view-classroom', views.view_classroom, name='view_classroom'),
    path('update-classroom/<id>/', views.update_classroom, name='update_classroom'),
    path('delete-classroom/<id>/',views.delete_classroom, name='delete_classroom'),
    
    path('add-batches', views.add_batches, name='add_batch'),
    path('view-batches', views.view_batches, name='view_batch'),
    path('update-batches/<id>/', views.update_batches, name='update_batch'),
    path('delete-batches/<id>/', views.delete_batches, name='delete_batch'),
    
    path('add-department', views.add_department, name='add_department'),
    path('view-department', views.view_department, name='view_department'),
    path('update-department/<id>/', views.update_department, name='update_department'),
    path('delete-department/<id>/', views.delete_department, name='delete_department'),

    path('add-timeslot', views.add_timeslot, name='add_timeslot'),
    path('view-timeslot', views.view_timeslots, name='view_timeslots'),
    path('update-timeslot/<id>/', views.update_timeslot, name='update_timeslot'),
    path('delete-timeslot/<id>/', views.delete_timeslot, name='delete_timeslot'),

    path('generate-timetable', views.timetable, name='generate_timetable'),

]