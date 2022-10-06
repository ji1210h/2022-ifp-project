from django.urls import path
from coffee import views
urlpatterns = [
    path('user/create/', views.UserCreateAPIView.as_view(), name='user-create'), # 회원가입
    path('user/login/', views.LoginAPIView.as_view(), name='user-login'), #로그인
    path('user/<int:pk>/',views.UserReadAPIView.as_view(), name='user-info'), #회원 정보 조회
    path('user/', views.UserRetrieveUpdateAPIView.as_view(), name='user') #내 정보 확인, 수정
] 
