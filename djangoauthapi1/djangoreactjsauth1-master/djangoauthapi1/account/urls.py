from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
from . import views
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path ('',views.ApiOverview, name='home'),
    path ('create/',views.add_products, name='add-products'),
    path ('all/',views.view_products, name='view_products'),
    path ('update/<int:pk>/', views.update_products, name='update-products'),
     path ('product/<int:pk>/delete', views.delete_products, name='delete-products'),
]