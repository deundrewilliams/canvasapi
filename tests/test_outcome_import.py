import unittest

import requests_mock

from canvasapi import Canvas
from canvasapi.outcome_import import OutcomeImport
from tests import settings

from tests import object_ids

@requests_mock.Mocker()
class TestOutcomeImport(unittest.TestCase):
    def setUp(self):
        self.canvas = Canvas(settings.BASE_URL, settings.API_KEY)

        self.outcome_import = OutcomeImport(
            self.canvas._Canvas__requester, {"id": object_ids.OUTCOME_IMPORT_ID, "workflow_state": 1}
        )

    def test_str(self, m):

        test_str = str(self.outcome_import)
        self.assertIsInstance(test_str, str)
