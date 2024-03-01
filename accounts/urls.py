from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLgoutView, UserBankAccountUpdateView, pass_change2
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',UserLgoutView.as_view(), name='logout'),
    path('profile/',UserBankAccountUpdateView.as_view(), name='profile'),
    path('passchange/', pass_change2, name='passchange'),

]