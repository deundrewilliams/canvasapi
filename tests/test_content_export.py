import unittest

import requests_mock

from canvasapi import Canvas
from tests import settings
from tests.util import register_uris

from tests import object_ids

@requests_mock.Mocker()
class TestContentExport(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(settings.BASE_URL, settings.API_KEY)

        with requests_mock.Mocker() as m:
            requires = {
                "course": ["get_by_id", "single_content_export"],
                "group": ["get_by_id", "single_content_export"],
                "user": ["get_by_id", "single_content_export"],
            }
            register_uris(requires, m)

            self.course = self.canvas.get_course(object_ids.COURSE_ID)
            self.group = self.canvas.get_group(object_ids.GROUP_ID)
            self.user = self.canvas.get_user(object_ids.USER_ID)

            self.content_export_course = self.course.get_content_export(object_ids.CONTENT_EXPORT_ID)
            self.content_export_group = self.group.get_content_export(object_ids.CONTENT_EXPORT_ID)
            self.content_export_user = self.user.get_content_export(object_ids.CONTENT_EXPORT_ID)

    # __str__()
    def test__str__(self, m):
        string = str(self.content_export_course)
        self.assertIsInstance(string, str)
