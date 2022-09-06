from django.urls import path
from . import views
urlpatterns = [
   path('',views.openForm),
   path('addemployee',views.saveEmployee),
   path('fetchall',views.getAllEmployees),
   path("delete/<int:id>",views.deleteEmployee),
   path("edit/<int:id>",views.openEditForm),
   path("update/<int:id>",views.updateEmployee)
]
