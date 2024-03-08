from .views import forgotpasswordView,registerView, loginView, emailValidation
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login',loginView.as_view(),name="login"),
    path('register',registerView.as_view(),name="register"),
    path('forgotpassword',forgotpasswordView.as_view(),name="forgotpassword"),
    path('validate_email',csrf_exempt(emailValidation.as_view()),name="validate_email"),
]