from django.urls import path
from . import views
urlpatterns =[
    path('',views.openLoginForm),
    path('dashboard',views.openDashboard),
    path('login',views.login),
    path('logout',views.logout),
    path('subjectform',views.openSubjectForm),
    path('viewsubjects',views.openSubjectslist),
    path('addsubject',views.addSubject),
    path("delete/<int:id>",views.deleteSubject),
    path("update/<int:id>",views.updateSubject),
    path("edit/<int:id>",views.openEditForm),
]


   