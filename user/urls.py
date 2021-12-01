# from django.urls import include, path
# from rest_framework import routers

from user import views

# urlpatterns = [
#     path('', UserView.as_view()),
# ]

from django.urls import path


urlpatterns = [
    path('login', views.user_login, name='login')
]