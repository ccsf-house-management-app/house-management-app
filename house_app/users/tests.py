from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import signup, signin, signout, users,UserInfoListView,UserInfoDetailView, UserInfoView,UserInfoDetailsView,UserViewSet

from .models import UserInfo
# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolve(self):
        url = reverse('signin')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signin)

#
# class BasicTest(TestCase):
#
#     def serUp(self):
#         self.UserInfo = UserInfo()
#         self.UserInfo.firstname = "First Name Test"
#         self.UserInfo.lastname = "Last Name Test"
#         self.UserInfo.birthdate = " Birthday Test"
#         self.UserInfo.email = "Email Test"
#         self.UserInfo.phone = "Email Test"
#         self.UserInfo.date_created = "Date created Test"
#         self.UserInfo.save()
#
#     def test_fields(self):
#         UserInfo = UserInfo()
#         UserInfo.firstname = "First Name Test"
#         UserInfo.lastname = "Last Name Test"
#         UserInfo.birthdate = " Birthday Test"
#         UserInfo.email = "Email Test"
#         UserInfo.phone = "Email Test"
#         UserInfo.date_created = "Date created Test"
#
#         record = UserInfo.objects.get(userid=UserInfo.userid)
#         self.assertEqual(record, UserInfo)
#
#     def test_get_absolite_url(self):
#         self.assertEqual(
#             self.UserInfo.get_absolute_url(),
#             "/%s-%s/" % (self.UserInfo.userid, self.UserInfo.slug)
#         )

