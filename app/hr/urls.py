from django.urls import path,include
from .views import UserApiView

urlpatterns = [
    path('api/<int:id>/', UserApiView.as_view()),
    path('api/', UserApiView.as_view()),

]