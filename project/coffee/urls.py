from django.urls import path
from coffee import views
urlpatterns = [
    path('user/create/', views.UserCreateAPIView.as_view(), name='user-create'), # 회원가입
    path('user/login/', views.LoginAPIView.as_view(), name='user-login'), #로그인
    path('user/<int:pk>/',views.UserReadAPIView.as_view(), name='user-info'), #회원 정보 조회
    path('user/', views.UserRetrieveUpdateAPIView.as_view(), name='user'), #내 정보 확인, 수정
    path('post/', views.PostListAPIView.as_view(), name="coffe"), # 글 목록들
    path('post/<int:pk>/', views.PostReadAPIView.as_view(), name="post"), #글 상세정보
    path('post/create/', views.PostCreateAPIView.as_view(), name='post-create') #글 작성
 ] 
