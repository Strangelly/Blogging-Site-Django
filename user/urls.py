from django.urls import path
from .views import UserRegister, UserEditView
from . import views

urlpatterns = [
   path('register/', UserRegister.as_view(),name='register'),
   path('login_user', views.login_user, name="login"),
   path('logout_user', views.logout_user, name= "logout" ),
   path('edit_profile/', UserEditView.as_view(),name='edit_profile'),
]
