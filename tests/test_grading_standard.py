import unittest

import requests_mock

from canvasapi import Canvas
from tests import settings
from tests.util import register_uris

from tests import object_ids

@requests_mock.Mocker()
class TestGradingStandard(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(settings.BASE_URL, settings.API_KEY)

        with requests_mock.Mocker() as m:
            register_uris({"course": ["get_by_id", "get_single_grading_standard"]}, m)

            self.course = self.canvas.get_course(object_ids.COURSE_ID)
            self.grading_standard = self.course.get_single_grading_standard(object_ids.GRADING_STANDARD_ID)

    # __str__()
    def test__str__(self, m):
        string = str(self.grading_standard)
        self.assertIsInstance(string, str)
