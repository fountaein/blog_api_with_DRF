
from datetime import date, datetime
import json

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase,APIClient

from blog_api.models import Category, Post


class TestCategoryEndPoint(APITestCase):

    def setUp(self):

        self.user = get_user_model()
        self.user.objects.create_user(
            'oluchi_testing',
            email='oluchiuser@test.com',
            password='oluchipassword'
        )

        self.token = Token.objects.create(user=User.objects.get(id=1))
        self.uri = '/api/v1/category/'
        self.client = APIClient( HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        self.params ={'title':"Data analyis"}

        self.category = Category.objects.create(title='Data Science')



    def test_create_category(self):
        response = self.client.post(self.uri,data=json.dumps(self.params),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content), {"id":2,"title":"Data analyis"})

    def test_get_category(self):
        response = self.client.get(self.uri,content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content),  [{"id":1,"title":"Data Science"}])

    def test_update_category(self):

        response = self.client.put('/api/v1/category/1', data=json.dumps(self.params),content_type='application/json')
        self.assertEqual(response.status_code, 301)
        self.assertNotEqual(response.content,[])


