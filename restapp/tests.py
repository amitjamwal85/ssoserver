from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from django.test.runner import DiscoverRunner


class NoDbTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database teardown defined in parent class """
        pass


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        register = {
            "username": "amit1",
            "email": "amit@gmail.com",
            "firstName": "Amit",
            "lastName": "Kumar",
            "password": "1234",
        }
        self.user = User.objects.create(username=register.get('username'))
        self.user.set_password(register.get('password'))
        self.user.first_name = register.get('firstName')
        self.user.last_name = register.get('lastName')
        self.user.email = register.get('email')
        self.user.save()

    def test_login(self):

        login_data = {
          "username": "amit1",
          "password": "1234"
        }

        res = self.client.post("/user/login/", login_data)
        self.assertEqual(res.status_code, 200)

        expected = {
            'email': 'amit@gmail.com',
            'username': 'amit1',
        }
        resp = res.json()
        del resp['token']
        self.assertDictEqual(expected, resp)

