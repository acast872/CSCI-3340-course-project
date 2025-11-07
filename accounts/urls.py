from django.urls import path
from .views import SignUpView, UserListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'), #Sign
    path('login/', UserListView.as_view(), name='user_manage'), #Account Manage Page

]