"""Test for the ``face_sender`` module."""

from django.test import TestCase
from django.http import HttpRequest
from django.contrib.messages.storage.fallback import FallbackStorage
from . import views

class FaceSenderTest(TestCase):
    """Test running single-case filter job."""

    def setUp(self):
        super().setUp()

    def test_face_sender(self, *args, **kwargs):

        request = HttpRequest()
        setattr(request, 'session', self.client.session)
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        request.method = 'POST'
        request.FILES['gmImage'] = open('face_sender/cdls_demo.png', "rb")
        response = views.FaceSenderView.post(self, request, *args, **kwargs)

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'error', response.content)
