from django.urls import path
from . import views

urlpatterns = [
    path('',view=views.home,name='home'),
    path('school_manage/',view=views.school_manage,name='school_manage'),
    path('login/',view=views.loginin,name='loginin'),
    path('logout/',view=views.logout,name='logout'),
    path('registration/',view=views.registration,name='registration'),
    path('student/',view=views.student,name='student'),
    path('delete/<int:id>/',view=views.delete,name='delete'),
    path('add_student/',view=views.add_student,name='add_student'),
    
    path('all_teacher/',view=views.all_teacher , name='all_teacher')
]
