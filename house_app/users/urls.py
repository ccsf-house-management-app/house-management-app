from django.urls import path
from .views import(
      users,
      signup,
      signin,
      signout,
      UserInfoListView,
      UserInfoDetailView

)

app_name = 'users'
urlpatterns =[
    path('users', users),
    path('signup', signup, name='signup'),
    path('signin', signin, name='login'),
    path('signout', signout, name='logout'),
    path('', UserInfoListView.as_view(), name='userinfo-list'),
    path('<int:userid>/', UserInfoDetailView.as_view(), name='userinfo-detail')
]