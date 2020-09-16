
from datetime import date, datetime

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog_api.models import Category, Post


class TestModel(APITestCase):


    @classmethod 
    def setUpTestData(cls):
        User = get_user_model()
        User.objects.create_user(
                'oluchi_testing',
                email='oluchiuser@test.com',
                password='oluchipassword'
            )
        category = Category.objects.create(title='Data Science')
        post = Post.objects.create(title = "Introduction to Machine Learning",
                                slug = "introduction-to-Machine-Learning",
                                author = User.objects.get(id=1),
                                body =  "Machine learning is a method of data analysis that automates analytical model building" +
                                        "It is a branch of artificial intelligence based on the idea that systems can"  +
                                        "learn from data, identify patterns and make decisions with minimal human intervention.",
                                status =  "draft",
                                created =  date.today(), 
                                category= Category.objects.get(id=1))


    def test_post_model(self):
        post=Post.objects.get(id=1)
        expected_object_name=f'{post.title}'
        self.assertNotEquals(expected_object_name,'Data Analysis')
        self.assertEquals(post.category.title,'Data Science')
        
    def test_user_model(self):
        user=User.objects.get(id=1)
        username=f'{user.username}'
        email=f'{user.email}'
        self.assertNotEquals(email,'example@org.com')
        self.assertEquals(username,'oluchi_testing')
        
    def test_category_model(self):
        category=Category.objects.get(id=1)
        expected_object_name=f'{category.title}'
        self.assertNotEquals(expected_object_name,'Data Analysis')
        
        
        
        
