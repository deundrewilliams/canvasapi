import unittest

import requests_mock

from canvasapi.canvas import Canvas
from canvasapi.enrollment import Enrollment
from tests import settings
from tests.util import register_uris

from tests import object_ids

@requests_mock.Mocker()
class TestEnrollment(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(settings.BASE_URL, settings.API_KEY)

        with requests_mock.Mocker() as m:
            requires = {"account": ["get_by_id"], "enrollment": ["get_by_id"]}
            register_uris(requires, m)

            self.account = self.canvas.get_account(object_ids.ACCOUNT_ID)
            self.enrollment = self.account.get_enrollment(object_ids.ENROLLMENT_ID)

    # __str__()
    def test__str__(self, m):
        string = str(self.enrollment)
        self.assertIsInstance(string, str)

    # deactivate()
    def test_deactivate(self, m):
        register_uris({"enrollment": ["deactivate"]}, m)

        target_enrollment = self.enrollment.deactivate("conclude")

        self.assertIsInstance(target_enrollment, Enrollment)

    def test_deactivate_invalid_task(self, m):
        with self.assertRaises(ValueError):
            self.enrollment.deactivate("finish")

    # reactivate()
    def test_reactivate(self, m):
        register_uris({"enrollment": ["reactivate"]}, m)

        target_enrollment = self.enrollment.reactivate()

        self.assertIsInstance(target_enrollment, Enrollment)
