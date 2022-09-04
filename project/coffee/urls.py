from django.urls import path
urlpatterns = [
    path('user/create/', views.UserCreateAPIView.as_view(), name='user-create')
]
