from django.urls import path
from coffee import views
urlpatterns = [
    path('user/create/', views.UserCreateAPIView.as_view(), name='user-create')
]
