from django.urls import path

from users.views import login_user, logout_user, register, activate, resend_activation

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('activate/<str:token>', activate, name='activate'),
    path('resend-activation/', resend_activation, name='resend-activation')
]
