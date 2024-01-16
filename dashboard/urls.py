from django.urls import path
from dashboard.views import dashboard, create_url, redirect_url, delete_url
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create/', create_url, name='create-url'),
    path('delete/<int:_id>/', delete_url, name='delete-url'),
    path("<str:short_url>/", redirect_url, name="redirect-url"),
]
