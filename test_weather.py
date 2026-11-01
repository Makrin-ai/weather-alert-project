import unittest
from weather_service import WeatherService, WeatherAlert


class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.service = WeatherService()
        self.service.update_weather(temperature=5.0, condition="Cloudy")

    def test_get_current_weather(self):
        self.assertEqual(self.service.get_temperature(), 5.0)

    def test_alert_triggered_below_threshold(self):
        self.service.update_weather(temperature=-5.0, condition="Snow")
        alert = WeatherAlert(threshold=-2.0)
        self.assertTrue(alert.check_alert(self.service))

    def test_no_alert_above_threshold(self):
        alert = WeatherAlert(threshold=-2.0)
        self.assertFalse(alert.check_alert(self.service))


if __name__ == "__main__":
    unittest.main()