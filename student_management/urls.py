# """
# URL configuration for student_management project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect
# from rest_framework.authtoken.views import obtain_auth_token

# def home_redirect(request):
#     return redirect('/api/')

# urlpatterns = [
#     path('', home_redirect, name='home'),
#     path('admin/', admin.site.urls),
#     path('api/', include('students.urls')),
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
#     path('api-auth/', include('rest_framework.urls')),
# ]
from django.contrib import admin
from django.urls import path, include
from students import views  # import your app views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Default root → main_page (not redirect to /api/)
    # path('', views.main_page, name='main_page'),
    path('', views.first_page, name='first_page'),    # Default → first page
    path('main/', views.main_page, name='main_page'), # Main page

    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
]
