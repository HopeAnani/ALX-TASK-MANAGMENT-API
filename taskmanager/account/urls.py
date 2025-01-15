from django.urls import path
from . import views
from .views import SignUpAPIView, SignInAPIView, SignOutAPIView

app_name = 'account'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('api/signup/', SignUpAPIView.as_view(), name='signup'),
    path('api/signin/', SignInAPIView.as_view(), name='signin'),
    path('api/signout/', SignOutAPIView.as_view(), name='signout'),
]