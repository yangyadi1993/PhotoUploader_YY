from django.test import TestCase, Client, RequestFactory
from .models import *
from .views import *


class get_list_test(TestCase):
    def get_lis(self):
        client = Client()
        response = client.get('/file_upload/get_list')
        self.assertTrue(response.status_code == 200)