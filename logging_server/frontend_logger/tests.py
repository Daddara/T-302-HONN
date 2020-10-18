import datetime
from django.test import TestCase, Client
from frontend_logger.models import FrontendEvent


class TestFrontendEvent(TestCase):
    def init(self):
        self.client = Client()

    # Create your tests here.
    def test_button_press_minimal(self):
        current = datetime.datetime.now().ctime()
        payload = {
            "event_type": "BUTTON_PRESS",
            "current_url": "www.researching-animal-crossing.com/yes",
            "event_meta": "{'json': 'awesome'}"
        }
        response = self.client.post('/frontend/event', payload)
        self.assertEqual(response.status_code, 200)
        try:
            event = FrontendEvent.objects.get(current_url="www.researching-animal-crossing.com/yes")
            self.assertTrue(event.event_time.ctime() >= current)
            self.assertEqual(event.event_type, 'BUTTON_PRESS')
            self.assertIsNone(event.user_id)
            self.assertEqual(event.current_url, "www.researching-animal-crossing.com/yes")
            self.assertEqual(event.event_meta, "{'json': 'awesome'}")
            self.assertIsNone(event.session_meta)
        except FrontendEvent.DoesNotExist:
            self.assertTrue(False)

    def test_js_error_extensive(self):
        current = datetime.datetime.now().ctime()
        payload = {
            "event_type": "JS_ERROR",
            "user_id": 2,
            "current_url": "www.boredbutton.com",
            "event_meta": "{'file': 'my_face.js', 'call_stack': 'Here and there and everywhere'}",
            "session_meta": "{'online_time': '5255423'}"
        }
        response = self.client.post('/frontend/event', payload)
        self.assertEqual(response.status_code, 200)
        try:
            event = FrontendEvent.objects.get(current_url="www.boredbutton.com")
            self.assertTrue(event.event_time.ctime() >= current)
            self.assertEqual(event.event_type, 'JS_ERROR')
            self.assertEqual(event.user_id, 2)
            self.assertEqual(event.current_url, "www.boredbutton.com")
            self.assertEqual(event.event_meta, "{'file': 'my_face.js', 'call_stack': 'Here and there and everywhere'}")
            self.assertEqual(event.session_meta, "{'online_time': '5255423'}")
        except FrontendEvent.DoesNotExist:
            self.assertTrue(False)

    def test_not_okay(self):
        payload = {
            "event_type": "WHO_AM_I",
            "current_url": "www.doesnt-matter.com",
            "event_meta": "Some data",
        }
        response = self.client.post('/frontend/event', payload)
        self.assertEqual(response.status_code, 400)
