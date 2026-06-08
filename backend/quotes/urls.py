from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.submit_quote, name='submit_quote'),
    path('health/', views.health_check, name='health_check'),
    path('test-email/', views.test_email, name='test_email'),
]
