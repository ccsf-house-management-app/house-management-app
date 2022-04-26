"""house_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# from house_app import house_app_users
#from administration import views
from users.views import signup, signin, signout, users,UserInfoListView,UserInfoDetailView, UserInfoView,UserInfoDetailsView,UserViewSet
from pages.views import home_view
from rooms.views import RoomAssignDetailView,RoomListView, RoomsView, RoomsAssignView,TenantRoomView
from expenses.views import UtilitiesView
from credits.views import CreditView
from accounts.views import AccountView

from house_app_users.views import MyTokenObtainPairView, RegisterView

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()
# router.register(r'login', UserViewSet, 'login')
router.register(r'users', UserInfoView, 'users')
# router.register(r'users/<int:userid>', UserInfoDetailsView, 'user')
router.register(r'rooms', RoomsView, 'rooms')
router.register(r'roomassign', RoomsAssignView, 'roomassign')
router.register(r'tenant', TenantRoomView, 'tenant')
router.register(r'expenses', UtilitiesView, 'expenses')
router.register(r'credits', CreditView, 'credits')
router.register(r'accounts', AccountView, 'accounts')
# router.register(
#     r'token', MyTokenObtainPairView, basename="token")


additional_routes = [
    'token/',
    'register/',
    'token/refresh/'
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    # path('users/', include('users.urls')),
    path('users/', users),
    path('users/signup/', signup, name='signup'),
    path('users/signin/', signin, name='login'),
    path('users/signout/', signout, name='logout'),
    path('', UserInfoListView.as_view(), name='userinfo-list'),
    path('users/<int:userid>/', UserInfoDetailView.as_view(), name='userinfo-detail'),
    path('rooms/', RoomListView.as_view(), name='room-list'),
  #  path('rooms/<int:tenantid>/', RoomAssignDetailView.as_view(), name='room-detail'),
    path('rooms/<int:tenantid>/', RoomAssignDetailView.as_view(), name='room-detail'),
]
