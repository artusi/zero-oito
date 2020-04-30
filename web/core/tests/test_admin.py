from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="super@tusi.com",
            password="tusao"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@tusi.com",
            password="tusao",
            name="Test user name"
        )

    def test_users_listed(self):
        """ Test that users are listed on user page """
        # /admin/core/zerooitouser
        url = reverse('admin:core_zerooitouser_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """User edit page works"""
        # /admin/core/zerooitouser/{id}
        url = reverse('admin:core_zerooitouser_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """User create page works"""
        url = reverse('admin:core_zerooitouser_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
