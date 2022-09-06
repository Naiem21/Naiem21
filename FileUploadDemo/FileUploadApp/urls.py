from django.urls import path
from . import views
urlpatterns = [
    path('',views.openForm),
    path('register',views.registerUser)
]