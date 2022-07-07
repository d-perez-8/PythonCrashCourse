import unittest
from city_country import get_city_country

class TestCityCountry(unittest.TestCase):
    """ Test for city and country correctly inputed """
    def test_city_country(self):
        """Does 'Santiago, Chile' work?"""
        formatted_city = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted = get_city_country('santiago', 'chile', population=500000)
        self.assertEqual(formatted, 'Santiago, Chile - population 500000')

if __name__ == '__main__':
    unittest.main()