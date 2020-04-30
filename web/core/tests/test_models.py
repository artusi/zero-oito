from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email"""
        email = "tusi@test.com"
        password = "pass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """Test email is normalized"""
        email = "tusi@TEST.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password='123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='123'
            )

    def test_create_new_super_user(self):
        """Test creating a new super user"""
        super_user = get_user_model().objects.create_superuser(
            email='super@user.com',
            password='123'
        )

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
