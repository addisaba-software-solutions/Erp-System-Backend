from django.urls import path,include
from .views import AccountRUD,AccountListAdd,LoginAPIView

urlpatterns = [
   path('account/<int:accountId>/', AccountRUD.as_view()),
   path('account/', AccountListAdd.as_view()),
   path('login/', LoginAPIView.as_view()),
] 