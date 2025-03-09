from django.urls import path

from src.accounts.views import LoginView, LogoutView, SessionView, UserViewSet

user_viewset = UserViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'patch': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('session/', SessionView.as_view(), name='session'),
    path('account/', user_viewset, name='user')
]