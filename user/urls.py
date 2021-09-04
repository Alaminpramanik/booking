from django.urls import path, include

from . import views

urlpatterns = [
    path('register', views.UserRegistrationApiView.as_view(), name='register'),
    path('profile/', views.UserProfileApiView.as_view(), name='profile'),
    path('profile/update/', views.UserProfileUpdateApiView.as_view(), name='profile-update'),
    path('<int:pk>/profile', views.ProfileApiView.as_view(), name='profile'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('logout/', views.LogoutApiView.as_view(), name='logout'),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    path('password-reset/', views.PasswordResetAPIView.as_view(),
         name="password-reset"),
    path('password-reset/<uidb64>/<token>/',
         views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', views.SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
      

]
