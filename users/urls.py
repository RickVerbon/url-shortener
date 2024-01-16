from django.urls import path

from users.views import login, register, activate

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('activate/<str:token>', activate, name='activate'),
]
