from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app1 import views

router = DefaultRouter()
router.register('students', views.Students)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/get_all', views.get_all_student, name='get_all'),
    path('api/create', views.create_student, name='create'),
    path('api/update/<int:id>', views.update_student, name='update'),
    path('api/delete/<int:id>', views.delete_student, name='delete'),
    path('', include(router.urls)),
]
