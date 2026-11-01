import unittest
from io import StringIO
import sys

from weather_service import WeatherService, WeatherAlert


class TestWeatherAcceptance(unittest.TestCase):
    """Приёмочные тесты, согласованные с заказчиком."""

    def test_frost_alert_triggered(self):
        """Сценарий 1: При -10°C и пороге -5°C — оповещение отправлено."""
        service = WeatherService()
        service.update_weather(temperature=-10.0, condition="Snow")
        alert = WeatherAlert(threshold=-5.0)

        captured = StringIO()
        sys.stdout = captured
        result = alert.check_alert(service)
        sys.stdout = sys.__stdout__

        self.assertTrue(result)
        self.assertIn("ВНИМАНИЕ", captured.getvalue())

    def test_no_alert_when_warm(self):
        """Сценарий 2: При +15°C и пороге -5°C — оповещения нет."""
        service = WeatherService()
        service.update_weather(temperature=15.0, condition="Sunny")
        alert = WeatherAlert(threshold=-5.0)

        self.assertFalse(alert.check_alert(service))


if __name__ == "__main__":
    unittest.main()