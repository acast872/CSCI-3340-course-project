from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Announcement

User = get_user_model()


class AnnouncementModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')

    def test_create_announcement(self):
        ann = Announcement.objects.create(title='T', content='C', author=self.user)
        self.assertEqual(ann.status, Announcement.STATUS_PENDING)
        self.assertIn('T', str(ann))
