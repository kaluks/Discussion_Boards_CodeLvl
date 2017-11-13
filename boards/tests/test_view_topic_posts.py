from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Discussion_Board, Discussion, Post
from ..views import topic_posts


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Discussion_Board.objects.create(name='Geriatrics', description='geriatrics board.')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        topic = Discussion.objects.create(subject='Hello, world', board=board, started_by=user)
        Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
        url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEquals(view.func, topic_posts)
