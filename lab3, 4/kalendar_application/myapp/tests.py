# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from myapp.models import Entry


class TestEntry(TestCase):

    def setUp(self):
        self.entry = Entry(
            name='name',
            author=User.objects.create(),
            date=timezone.now(),
            description="this should be a long description...",
            participants = User.objects.all()

        )

    def test_short_description(self):
        self.assertEquals(self.entry.short_description(), 'this should be ')
