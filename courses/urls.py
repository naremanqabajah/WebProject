from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  # تعديل المسار الرئيسي ليكون صفحة تسجيل الدخول
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('add_course/', views.add_course, name='add_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('search_course/', views.search_course, name='search_course'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search_course, name='search_course'),
]


