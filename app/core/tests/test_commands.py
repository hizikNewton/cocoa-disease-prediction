from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import operationalError
from django.test import TestCase


class commandTest(TestCase):

    def test_wait_for_db_ready(self):
        with patch('django.db.utils.connectionhandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count,1)

    @patch('time.sleep',return_value = True):
    def test_unit_for_db(self,ts):
        with patch('django.db.utils.connectionhandler.__getitem__') as gi:
            gi.side_effect = [operationalError]*5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count,6)
