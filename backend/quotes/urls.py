from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.submit_quote, name='submit_quote'),
]
