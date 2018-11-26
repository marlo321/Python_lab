
from django.urls import reverse
from django.urls import resolve
from django.http import HttpRequest
from django.test import TestCase
from myapp.views import add
from myapp.views import IndexTemplateView
from myapp.views import signup
from myapp.views import home_page
class EntryTest(TestCase):

    def test_root_url_resolves_to_home_page_view1(self):
        resolver = resolve('/signup')
        self.assertEqual(resolver.func, signup)

    def test_root_url_resolves_to_home_page_view2(self):
        resolver = resolve('/entry/add')
        self.assertEqual(resolver.func, add)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)