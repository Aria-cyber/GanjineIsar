
from django.urls import path

from .views import RegisterView , GetToken

urlpatterns = [
    path('register' , RegisterView.as_view()),
    path('gettoken' , GetToken.as_view()),


]
