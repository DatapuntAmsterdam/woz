# Python
import logging

# Packages
from rest_framework.test import APITestCase
from woz.wozdata import woz_import

log = logging.getLogger(__name__)


class TestWaardeView(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        woz_import.import_woz_files('/app/data/fixtures')

    def test_get_no_paramater(self):
        response = self.client.get('/woz/waarde/')
        self.assertEqual(response.status_code, 400)

    def test_get_wrong_paramater(self):
        response = self.client.get('/woz/waarde/?kadastraal_object=ASD15 S 09256 A')
        self.assertEqual(response.status_code, 400)

    def test_get_non_existent_kadastraal_object(self):
        response = self.client.get('/woz/waarde/?kadastraal_object=ASD15 S 09256 A 0003')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, len(response.data['woz_waarden']))

    def test_get_kadastraal_object1(self):
        response = self.client.get('/woz/waarde/?kadastraal_object=ASD15 S 09256 A 0002')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('ASD15 S 09256 A 0002', response.data['kadastraal_object'])
        self.assertEqual(1, len(response.data['woz_waarden']))
        self.assertEqual('036398765431', response.data['woz_waarden'][0]['woz_object'])
        self.assertEqual(166000, response.data['woz_waarden'][0]['waarden'][2014])
        self.assertEqual(181000, response.data['woz_waarden'][0]['waarden'][2015])

    def test_get_kadastraal_object2(self):
        response = self.client.get('/woz/waarde/?kadastraal_object=ASD15 S 09256 A 0093')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('ASD15 S 09256 A 0093', response.data['kadastraal_object'])
        self.assertEqual(1, len(response.data['woz_waarden']))
        self.assertEqual('036398765431', response.data['woz_waarden'][0]['woz_object'])
        self.assertEqual(166000, response.data['woz_waarden'][0]['waarden'][2014])
        self.assertEqual(181000, response.data['woz_waarden'][0]['waarden'][2015])

    def test_get_kadastraal_object_new_price(self):
        response = self.client.get('/woz/waarde/?kadastraal_object=ASD15 S 09256 A 0013')
        self.assertEqual('ASD15 S 09256 A 0013', response.data['kadastraal_object'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(response.data['woz_waarden']))
        self.assertEqual('036398765432', response.data['woz_waarden'][0]['woz_object'])
        self.assertEqual(167000, response.data['woz_waarden'][0]['waarden'][2014])
        self.assertEqual(179000, response.data['woz_waarden'][0]['waarden'][2015])

    def test_get_kadastraal_object_multiple_woz_objects(self):
        response = self.client.get('/woz/waarde/?kadastraal_object=ASD15 S 04638 G 0000')
        self.assertEqual('ASD15 S 04638 G 0000', response.data['kadastraal_object'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, len(response.data['woz_waarden']))
        self.assertEqual('036398765433', response.data['woz_waarden'][0]['woz_object'])
        self.assertEqual(294500, response.data['woz_waarden'][0]['waarden'][2014])
        self.assertEqual(236500, response.data['woz_waarden'][0]['waarden'][2015])
        self.assertEqual('036398765434', response.data['woz_waarden'][1]['woz_object'])
        self.assertEqual(285500, response.data['woz_waarden'][1]['waarden'][2014])
        self.assertEqual(229500, response.data['woz_waarden'][1]['waarden'][2015])

    def test_get_non_woonfunctie_kadastraal_object6(self):
        response = self.client.get('/woz/waarde/?kadastraal_object=ASD15 S 04639 G 0000')
        self.assertEqual('ASD15 S 04639 G 0000', response.data['kadastraal_object'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(response.data['woz_waarden']))
