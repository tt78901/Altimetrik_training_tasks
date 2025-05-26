from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'performances', views.PerformanceViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-performance/', views.add_performance, name='add_performance'),
    path('view-performance/', views.view_performance, name='view_performance'),
    path('performance-charts/', views.performance_charts, name='performance_charts'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete-student/<int:pk>/', views.delete_student, name='delete_student'),
    path('update-student/<int:pk>/', views.update_student, name='update_student'),
]
