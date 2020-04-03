from django.urls import path, include
from . import views

urlpatterns = [
    path('phone-number/sent/', views.PhoneNumberView.as_view()),
    path('resend/<int:phonenumber_id>/confirmation/', views.ResendConfirmationView.as_view()),
    path('phone-number/confirmation/', views.PINConfirmationView.as_view()),
]