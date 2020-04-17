from django.urls import path, include
from .views import AccountRUD, AccountListAdd, LoginAPIView

urlpatterns = [
    path("api/v1/account/<int:accountId>/", AccountRUD.as_view()),
    path("api/v1/account/", AccountListAdd.as_view()),
    path("api/v1/login/", LoginAPIView.as_view()),
]
